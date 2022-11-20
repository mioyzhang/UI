import os
import json
import socket
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

        self.udp_port = None
        self.tcp_port = None
        self.tcpServer = socket.socket()
        self.tcpClient = socket.socket()
        self.udpReceiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udpSender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_packet(self, packet: Packet, address):
        self.tcp_port = get_port()
        thread = Thread(target=self.tcp_transfer, args=(self.tcp_port, packet.message))
        thread.start()

        message = {
            'type': PACKET_LINK,
            'protocol': 'TCP',
            'port': self.tcp_port
        }
        self.udpSender.sendto(json.dumps(message).encode(), address)

        recvData, addr = self.udpSender.recvfrom(BUFFER_SIZE)
        info = json.loads(recvData.decode())
        print(f'recv {info}')

        if info.get('status'):
            print('ready')

    def tcp_transfer(self, port, message: Message):
        server = socket.socket()
        server.bind(('0.0.0.0', port))
        print(f'tcp listen on port {port}')
        server.listen(5)
        client, address = server.accept()

        msg = message.to_json(with_path=False)
        client.send(msg.encode())

        files = message.images + message.files
        for i in files:
            self.send_file(i)

    def send_file(self):
        pass

    def test_connect(self, address):
        try:
            test_msg = {
                'type': PACKET_TEST,
                'time': time.time(),
                'hostname': HostName
            }
            message = json.dumps(test_msg)
            self.udpSender.sendto(message.encode(), address)
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
                return True, back
            else:
                raise ConnectionError('ConnectionError')

        except BaseException as e:
            back = {
                'type': OUT_ERROR,
                'status': CONNECT_FAIL,
                'error': str(e)
            }
            print(e)
            return False, back

    def udp_recv(self):
        try:
            self.udpReceiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.udpReceiver.bind(('0.0.0.0', LISTENING_PORT))
            print(f'UDP listen on port {LISTENING_PORT}')
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
            print(f'send {info} back\n')

            signal = {
                'type': OUT_INFO,
                'status': TEST_DELAY,
                'hostname': info.get('hostname'),
                'ip_address': addr[0],
                'port': addr[1],
                'recv_time': time.time(),
            }
            self.trigger_out.emit(signal)

        if type_ == PACKET_LINK:
            print(f'recv connection request from {addr}')
            ip = addr[0]
            port = info.get('port')
            back = {
                'type': PACKET_LINK,
                'status': True
            }
            print(f'try to connect to {ip}:{port}')
            self.tcpClient.connect((ip, port))

            self.udpReceiver.sendto(json.dumps(back).encode(), addr)
            print('connect success')

        if type_ in [PACKET_NONE, PACKET_DETECT, PACKET_ORDER, PACKET_REPLY]:
            print(f'recv message type {type_}')
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
                # todo


def get_port():
    sock = socket.socket()
    sock.bind(('0.0.0.0', 0))
    _, port = sock.getsockname()
    sock.close()
    return port


if __name__ == '__main__':
    s = TransferThread()
    s.udp_recv()
    pass

