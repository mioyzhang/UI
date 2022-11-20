import os
import json
import socket
import threading
from math import ceil
from threading import Thread

from PyQt5.QtCore import QThread, pyqtSignal

from tools import *


class RecvThread(Thread):
    def __init__(self, client: socket.socket, addr):
        super().__init__()
        self.client = client
        self.addr = addr

    def run(self):
        while True:
            try:
                content = self.client.recv(1024).decode('utf-8')

                if not content:
                    print(f'{self.addr} disconnect')
                    self.client.close()
                    break

                info = json.loads(content)
                print(f'recv: {info}')

                if not isinstance(info, dict):
                    print(info)
                    continue

                type_ = info.get('type')
                if type_ == PACKET_TEST:
                    print(f'{self.addr} recv {content}')
                    self.client.send(content.encode())
                
                if type_ == PACKET_FILE:

                    self.client.send('ready'.encode())

                    file_name = info.get('file_name')
                    file_size = info.get('file_size')
                    file_path = os.path.join(save_path, file_name)
                    print(f'recv {file_name} {file_size} byte')
                    
                    with open(file_path, 'wb') as f:
                        for i in range(ceil(file_size / Buffersize)):
                            bytes_read = self.client.recv(Buffersize)
                            if not bytes_read:
                                break
                            f.write(bytes_read)

                    print(f'recv {file_name}')
                    self.client.send('finish'.encode())
            except BaseException as e:
                print(e)
                raise e


def r():
    server = socket.socket()
    server.bind(('0.0.0.0', 8900))
    server.listen(32)

    while True:
        server.settimeout(None)
        client, address = server.accept()
        client.settimeout(None)
        print(f'{address} connected')
        p = RecvThread(client, address)
        p.start()


if __name__ == '__main__':
    Buffersize = 4096*10
    # save_path = '/home/dell/workspace/tmp'
    save_path = 'D:/Develop/PycharmProjects/UI/resource/tmp'
    r()
