import os
import json
import socket
import time
from math import ceil
from threading import Thread

from PyQt5.QtCore import QObject, pyqtSignal

from tools import *
from logic import Packet, Message


class TransferThread(QObject):
    trigger_start = pyqtSignal()
    trigger_in = pyqtSignal(dict)
    trigger_out = pyqtSignal(dict)

    def __init__(self, udp_port=LISTENING_PORT):
        super(TransferThread, self).__init__()
        self.udp_port = udp_port
        self.tcp_port = None
        self.udpReceiver = None
        self.udpSender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def slot(self, args):
        type_ = args.get('type')

        if type_ == SIGNAL_CHECK:
            address = args.get('address')
            print(f'test connect to {address}')
            self.test_connect(address)
            
        if type_ == SIGNAL_SEND:
            address = args.get('dest')
            content = args.get('content')
            protocol = args.get('protocol')
            message = Message(content)
            print(f'send {message} to {address}')
            self.send_message(message, address)

    def send_message(self, message, address):
        try:
            self.tcp_port = get_port()

            msg = {
                'type': PACKET_LINK,
                'protocol': 'TCP',
                'port': self.tcp_port
            }
            self.udpSender.sendto(json.dumps(msg).encode(), address)

            recvData, addr = self.udpSender.recvfrom(BUFFER_SIZE)
            info = json.loads(recvData.decode())
            type_ = info.get('type')
            if type_ == PACKET_LINK_BACK:
                print('waiting for connection')

            thread = Thread(target=self.tcp_transfer_send, args=(self.tcp_port, message))
            thread.start()

        except BaseException as e:
            signal = {
                'type': OUT_ERROR,
                'status': SEND_ERROR,
                'content': str(message),
                'error': e,
            }
            print(e)
            self.trigger_out.emit(signal)

    def tcp_transfer_send(self, port, message: Message):
        server = None
        try:
            server = socket.socket()
            server.bind(('0.0.0.0', port))
            print(f'tcp waiting on port {port}')
            server.listen(5)
            client, address = server.accept()

            print('start send messages')
            msg = message.to_json(with_path=False)
            client.send(msg.encode())
            back = client.recv(BUFFER_SIZE).decode()

            files = message.images + message.files
            for i in files:
                self.send_file(i, client, address)
            
            print(f'send {message} success')
            # signal 8
            signal = {
                'type': OUT_SEND,
                'status': SEND_SUCCESS,
                'content': message.to_json(),
                'ip_address': address[0],
                'flow': TX,
                'send_time': time.time()
            }
            self.trigger_out.emit(signal)
        except BaseException as e:
            # signal
            signal = {
                'type': OUT_ERROR,
                'status': SEND_ERROR,
                'content': message.to_dict(),
                'error': e,
            }
            self.trigger_out.emit(signal)
            raise e
        finally:
            server.close()
            
    def send_file(self, file, client, address):
        file_name = os.path.basename(file)
        file_size = os.path.getsize(file)
        msg = {
            'type': PACKET_FILE,
            'file_name': file_name,
            'file_size': file_size
        }
        print(f'send {file_name} {file_size} byte to {address}')
        client.send(json.dumps(msg).encode())
        back = client.recv(BUFFER_SIZE).decode()

        with open(file, 'rb') as f:
            while True:
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    break
                client.sendall(bytes_read)

        back = client.recv(BUFFER_SIZE).decode()
        print(f'send {file_name} success')

    def tcp_transfer_recv(self, address):
        try:
            print(f'try to connect to {address[0]}:{address[1]}')
            client = socket.socket()
            client.connect(address)
            print('start recv messages')
            content = client.recv(BUFFER_SIZE).decode()

            back = {'type': PACKET_TOOL, 'status': True}
            client.send(json.dumps(back).encode())

            info = json.loads(content)
            files = info.get('files') + info.get('images')
            print(f'recv {info}')
            for _ in files:
                content = client.recv(BUFFER_SIZE).decode()

                back = {'type': PACKET_TOOL, 'status': True}
                client.send(json.dumps(back).encode())
                
                file_info = json.loads(content)
                type_ = file_info.get('type')
                if type_ not in [PACKET_FILE, PACKET_IMG]:
                    print('type_ not in [PACKET_FILE, PACKET_IMG]')
                    pass
                file_name = file_info.get('file_name')
                file_size = file_info.get('file_size')

                file_path = os.path.join(SAVE_PATH, file_name)
                with open(file_path, 'wb') as f:
                    for i in range(ceil(file_size / BUFFER_SIZE)):
                        bytes_read = client.recv(BUFFER_SIZE)
                        f.write(bytes_read)

                back = {'type': PACKET_TOOL, 'file': file_name, 'status': True}
                client.send(json.dumps(back).encode())
                print(f'recv {file_name} {file_size} byte')
            
            print(f'recv Message({info.get("sequence")}) success')
            # signal 5
            signal = {
                'type': OUT_RECV,
                'status': RECV_SUCCESS,
                'content': info,
                'ip_address': address[0],
                'flow': RX,
                'recv_time': time.time()
            }
            self.trigger_out.emit(signal)
        except BaseException as e:
            # signal 6
            signal = {
                'type': OUT_ERROR,
                'status': RECV_ERROR,
                'error': e,
            }
            self.trigger_out.emit(signal)
        finally:
            client.close()

    def test_connect(self, address):
        try:
            print(f'test delay to {address}')
            test_msg = {
                'type': PACKET_TEST,
                'time': time.time(),
                'hostname': HostName
            }
            message = json.dumps(test_msg)
            self.udpSender.sendto(message.encode(), address)
            self.udpSender.settimeout(TIMEOUT)
            recvData, addr = self.udpSender.recvfrom(BUFFER_SIZE)

            back = json.loads(recvData.decode())
            type_ = back.get('type')

            if type_ == PACKET_TEST:
                past_time = back.get('time')
                hostname = back.get('hostname')
                delay = time.time() - past_time
                # signal 7
                back = {
                    'type': OUT_INFO,
                    'status': TEST_DELAY,
                    'hostname': hostname,
                    'address': address,
                    'delay': delay,
                }
                print(f'connect to {addr} delay {delay}s')
                self.trigger_out.emit(back)
            else:
                raise ConnectionError('ConnectionError recv wrong type packet')

        except BaseException as e:
            # signal 8
            signal = {
                'type': OUT_ERROR,
                'status': TEST_DELAY_FAIL,
                'ip_address': address[0],
                'error': str(e)
            }
            self.trigger_out.emit(signal)
            print(e)

    def udp_accept(self):
        try:
            self.udpReceiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.udpReceiver.bind(('0.0.0.0', self.udp_port))
            print(f'UDP listen on port {self.udp_port}')

            # signal 1
            signal = {
                'type': OUT_INFO,
                'status': INIT_ACCEPT_SUCCESS,
                'port': self.udp_port
            }
            self.trigger_out.emit(signal)

            while True:
                recData, addr = self.udpReceiver.recvfrom(BUFFER_SIZE)
                recData = json.loads(recData)
                print(f'recv {addr} {recData}')
                self.process(recData, addr)

        except BaseException as e:
            # signal 2
            signal = {
                'type': OUT_ERROR,
                'status': ACCEPT_ERROR,
                'error': e
            }
            self.trigger_out.emit(signal)
            print(e)

    def process(self, info, addr):
        type_ = info.get('type')
        if type_ == PACKET_TEST:
            print(f'recv test packet {addr}')

            # signal 3
            signal = {
                'type': OUT_INFO,
                'status': OTHER_TEST_DELAY,
                'hostname': info.get('hostname'),
                'ip_address': addr[0],
                'port': addr[1],
                'recv_time': time.time(),
            }
            self.trigger_out.emit(signal)

            info['hostname'] = HostName
            self.udpReceiver.sendto(json.dumps(info).encode(), addr)
            print(f'send {info} back')

        if type_ == PACKET_LINK:
            print(f'recv connect request from {addr}')

            message = {'type': PACKET_LINK_BACK, 'status': True}
            self.udpSender.sendto(json.dumps(message).encode(), addr)

            ip, port = addr[0], info.get('port')
            thread = Thread(target=self.tcp_transfer_recv, args=((ip, port), ))
            thread.start()

            # signal 4
            signal = {
                'type': OUT_INFO,
                'status': RECV_CONNECTION,  # ?
                'address': (ip, port)
            }
            self.trigger_out.emit(signal)


def get_port():
    sock = socket.socket()
    sock.bind(('0.0.0.0', 0))
    _, port = sock.getsockname()
    sock.close()
    return port


if __name__ == '__main__':
    s = TransferThread()
    s.udp_accept()
    pass

