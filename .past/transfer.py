import os
import json
import time
from math import ceil
from retrying import retry
from threading import Thread

from PyQt5.QtCore import QObject, pyqtSignal

from tools import *
from logic import Packet, Message


class TransferThread(QObject):
    trigger_start = pyqtSignal()
    trigger_in = pyqtSignal(dict)
    trigger_out = pyqtSignal(dict)

    def __init__(self):
        super(TransferThread, self).__init__()

        self.client = socket.socket()
        self.server = socket.socket()

        self.connected = None
        self.connections = []

    def slot(self, args: dict):
        type_ = args.get('type')
        print(f'Thread <-- signal {type_}')

        if type_ == SIGNAL_SEND:
            dest = args.get('dest')
            content = args.get('content')

            msg = Message(content)
            pkg = Packet(dst=dest, message=msg)
            self.send_packet(pkg)

        if type_ == SIGNAL_CHECK:
            address = args.get('address')
            self.check_delay(address)

        if type_ == SIGNAL_TEST:
            print('SIGNAL_TEST')

    def re_client(self):
        self.client.close()
        self.client = socket.socket()
        self.connected = None

    def connect(self, address):
        """
        尝试连接到服务端
        :param address:
        :return:
        """
        try:
            if self.connected and self.connected != address:
                print(f'disconnect {self.connected}')
                self.re_client()

            if not self.connected:
                self.client.connect(address)
                self.connected = address
                print(f'connect to {self.connected}')

            test_msg = {
                'type': PACKET_TEST,
                'time': time.time(),
                'hostname': HostName
            }
            message = json.dumps(test_msg)
            status, back = self.send(message)

            if status:
                status, back = self.recv()
                type_ = back.get('type')
                if status and type_ == PACKET_TEST:
                    past_time = back.get('time')
                    hostname = back.get('hostname')
                    delay = time.time() - past_time
                    back = {
                        'status': TEST_DELAY,
                        'hostname': hostname,
                        'address': address,
                        'delay': delay,
                    }
                    print(f'connect to {self.connected} delay {delay}s')
                    return True, back
            raise ConnectionError('connection error')

        except BaseException as e:
            back = {
                'status': CONNECT_FAIL,
                'error': str(e)
            }
            print(e)
            self.re_client()
            return False, back

    def check_delay(self, address):
        status, back = self.connect(address)
        if status:
            back['type'] = OUT_INFO
            self.trigger_out.emit(back)
        else:
            back['type'] = OUT_ERROR
            self.trigger_out.emit(back)

    def send_packet(self, packet: Packet):
        print(f'try to send {packet}')
        ipaddress, port = packet.dst
        status, back = self.connect((ipaddress, port))
        if not status:
            back['type'] = OUT_ERROR
            self.trigger_out.emit(back)
            return False

        msg = packet.message.to_json(with_path=False)
        status, back = self.send(msg)
        if not status:
            back['type'] = OUT_ERROR
            self.trigger_out.emit(back)
            return False

        files = packet.message.images + packet.message.files
        for i in files:
            status, back = self.send_file(i)
            if not status:
                back['type'] = OUT_SEND
                self.trigger_out.emit(back)
                return False
        print(f'send {packet} success')

    def send(self, message):
        try:
            self.client.send(message.encode())
            back = {
                'status': SEND_SUCCESS,
                'content': message
            }
            print(f'send {message} to {self.connected}')
            return True, back
        except BaseException as e:
            back = {
                'status': SEND_ERROR,
                'content': message,
                'error': str(e)
            }
            print(f'send {message} to {self.connected} fail')
            self.re_client()
            return False, back

    def send_file(self, file):
        file_name = os.path.basename(file)
        file_size = os.path.getsize(file)
        msg = {
            'type': PACKET_FILE,
            'file_name': file_name,
            'file_size': file_size
        }

        print(f'send {file_name} {file_size} byte to {self.connected}')

        try:
            self.client.send(json.dumps(msg).encode())
            r = self.client.recv(2048)
            if not r:
                raise ConnectionError('server not ready')

            with open(file, 'rb') as f:
                while True:
                    bytes_read = f.read(BUFFER_SIZE)
                    if not bytes_read:
                        break
                    self.client.sendall(bytes_read)

            r = self.client.recv(2048)
            if not r:
                raise ConnectionError('send fail')
            print(f'send {file_name} success')

            return True, None

        except BaseException as e:
            back = {
                'status': SEND_ERROR,
                'content': f'Failed to send {file_name}',
                'error': str(e)
            }
            print(f'Failed to send {file_name}')
            print(e)
            self.re_client()
            return False, back

    def recv(self):
        try:
            message = self.client.recv(2048).decode()
            message = json.loads(message)
            return True, message
        except BaseException as e:
            back = {
                'status': RECV_ERROR,
                'error': e
            }
            self.re_client()
            return False, back

    def accept(self):
        try:
            self.server.bind(('0.0.0.0', LISTENING_PORT))
            self.server.listen(32)
            print(f'Listening on port {LISTENING_PORT}')

            signal = {
                'type': OUT_INFO,
                'status': INIT_ACCEPT_SUCCESS,
                'port': LISTENING_PORT
            }
            self.trigger_out.emit(signal)

            # to be processed
            self.server.settimeout(None)
            while True:
                client, address = self.server.accept()
                client.settimeout(None)
                print(f'connect from {address}')
                signal = {
                    'type': OUT_INFO,
                    'status': RECV_CONNECTION,
                    'ip_address': address[0],
                    'port': address[1],
                }
                self.trigger_out.emit(signal)
                thread = Thread(target=self.recv_process, args=(client, address))
                thread.start()
                thread.join()

        except BaseException as e:
            signal = {
                'type': OUT_ERROR,
                'error': e
            }
            self.trigger_out.emit(signal)
            raise e

        finally:
            self.server.close()

    def recv_process(self, client, addr):
        try:
            while True:
                content = client.udp_recv(BUFFER_SIZE).decode('utf-8')
                if not content:
                    raise ConnectionError('recv wrong buf')

                info = json.loads(content)

                type_ = info.get('type')
                if type_ == PACKET_TEST:
                    print(f'recv test packet {addr}')
                    info['hostname'] = HostName
                    client.send(json.dumps(info).encode())
                    print(f'send {info} back')

                    signal = {
                        'type': OUT_INFO,
                        'status': TEST_DELAY,
                        'hostname': info.get('hostname'),
                        'ip_address': addr[0],
                        'port': addr[1],
                        'recv_time': time.time(),
                    }
                    self.trigger_out.emit(signal)

                if type_ in [PACKET_NONE, PACKET_DETECT, PACKET_ORDER, PACKET_REPLY]:
                    print(f'recv message type {type_} length {len(content)}')
                    signal = {
                        'type': OUT_RECV,
                        'status': RECV_MESSAGE,
                        'content': info,
                        'ip_address': addr[0],
                        'port': addr[1],
                        'flow': RX,
                        'recv_time': time.time()
                    }
                    self.trigger_out.emit(signal)
                    if info.get('images') or info.get('files'):
                        print(info.get('images'))
                        print(info.get('files'))

                if type_ == PACKET_FILE:
                    msg = {
                        'type': PACKET_BACK,
                        'status': TRANSFER_READY
                    }
                    client.send(json.dumps(msg).encode())
                    file_name = info.get('file_name')
                    file_size = info.get('file_size')
                    file_path = os.path.join(SAVE_PATH, file_name)
                    print(f'recv {file_name} {file_size} byte')

                    with open(file_path, 'wb') as f:
                        for i in range(ceil(file_size / BUFFER_SIZE)):
                            bytes_read = client.udp_recv(BUFFER_SIZE)
                            if not bytes_read:
                                break
                            f.write(bytes_read)

                    print(f'recv {file_name}')
                    msg = {
                        'type': PACKET_BACK,
                        'status': TRANSFER_FINISH
                    }
                    client.send(json.dumps(msg).encode())

        except BaseException as e:
            client.close()
            print(e)
            raise e


if __name__ == '__main__':
    # t = Transfer()
    # t.accept()
    t = TransferThread()
    t.start()
    t.exec()
