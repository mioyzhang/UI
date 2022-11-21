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
            self.test_connect(address)
            
        if type_ == SIGNAL_SEND:
            address = args.get('dest')
            content = args.get('content')
            protocol = args.get('protocol')
            message = Message(content)
            self.send_message(message, address)

    def send_message(self, message, address):
        self.tcp_port = get_port()
        thread = Thread(target=self.tcp_transfer_send, args=(self.tcp_port, message))
        thread.start()

        message = {
            'type': PACKET_LINK,
            'protocol': 'TCP',
            'port': self.tcp_port
        }
        self.udpSender.sendto(json.dumps(message).encode(), address)

        recvData, addr = self.udpSender.recvfrom(BUFFER_SIZE)
        info = json.loads(recvData.decode())
        if info.get('status'):
            print('waiting for connection')

    def tcp_transfer_send(self, port, message: Message):
        try:
            server = socket.socket()
            server.bind(('0.0.0.0', port))
            print(f'tcp listen on port {port}')
            server.listen(5)
            client, address = server.accept()

            msg = message.to_json(with_path=False)
            client.send(msg.encode())
            back = client.recv(BUFFER_SIZE).decode()

            files = message.images + message.files
            for i in files:
                self.send_file(i, client, address)
            
            print(f'send {message} success')
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
        r = client.recv(2048)

        with open(file, 'rb') as f:
            while True:
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    break
                client.sendall(bytes_read)

        r = client.recv(2048)
        print(f'send {file_name} success')

    def tcp_transfer_recv(self, address):
        try:
            client = socket.socket()
            client.connect(address)
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
                file_name = file_info.get('file_name')
                file_size = file_info.get('file_size')
                file_path = os.path.join(save_path, file_name)
                print(f'recv {file_name} {file_size} byte')

                with open(file_path, 'wb') as f:
                    for i in range(ceil(file_size / BUFFER_SIZE)):
                        bytes_read = client.recv(BUFFER_SIZE)
                        if not bytes_read:
                            break
                        f.write(bytes_read)
                back = {'type': PACKET_TOOL, 'file':file_name, 'status': True}
                client.send(json.dumps(back).encode())
            
            print(f'recv {info} success')
            signal = {
                'type': OUT_SEND,
                'status': SEND_SUCCESS,
                'content': info,
                'ip_address': address[0],
                'flow': RX,
                'recv_time': time.time()
            }
            self.trigger_out.emit(signal)
        except BaseException as e:
            signal = {
                'type': OUT_ERROR,
                'status': SEND_ERROR,
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
                back = {
                    'type': OUT_INFO,
                    'status': TEST_DELAY,
                    'hostname': hostname,
                    'address': address,
                    'delay': delay,
                }
                print(f'connect to {addr} delay {delay}s')
                self.trigger_out.emit(back)
                return True, back
            else:
                raise ConnectionError('ConnectionError')

        except BaseException as e:
            back = {
                'type': OUT_ERROR,
                'status': TEST_DELAY_FAIL,
                'error': str(e)
            }
            print(e)
            self.trigger_out.emit(back)
            return False, back

    def udp_accept(self):
        try:
            self.udpReceiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.udpReceiver.bind(('0.0.0.0', self.udp_port))
            print(f'UDP listen on port {self.udp_port}')
            while True:
                recData, addr = self.udpReceiver.recvfrom(BUFFER_SIZE)
                recData = json.loads(recData)
                print(f'recv {addr} {recData}')
                self.process(recData, addr)

        except BaseException as e:
            signal = {
                'type': OUT_ERROR,
                'error': e
            }
            self.trigger_out.emit(signal)
            raise e

    def process(self, info, addr):
        type_ = info.get('type')
        if type_ == PACKET_TEST:
            print(f'recv test packet {addr}')
            info['hostname'] = HostName
            self.udpReceiver.sendto(json.dumps(info).encode(), addr)
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
            print(f'out  signal {signal}\n')

        if type_ == PACKET_LINK:
            print(f'recv send request from {addr}')
            ip = addr[0]
            port = info.get('port')
            print(f'try to connect to {ip}:{port}')
            thread = Thread(target=self.tcp_transfer_recv, args=((ip, port), ))
            thread.start()

            back = { 'type': PACKET_LINK, 'status': True}
            self.udpReceiver.sendto(json.dumps(back).encode(), addr)
            print('connect success')


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

