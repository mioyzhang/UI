import os
import json
import socket
import threading
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
                print(info)

                if not isinstance(info, dict):
                    print(info)
                    continue

                type_ = info.get('type')
                if type_ == PACKET_TEST:
                    print(f'{self.addr} recv {content}')
                    self.client.send(content.encode())
                
                if type_ == PACKET_FILE:
                    file_name = info.get('file_name')
                    file_size = info.get('file_size')
                    print(f'recv {file_name} {file_size}byte')
                    file_path = os.path.join(save_path, file_name)
                    
                    with open(file_path, 'rb') as f:

                        bytes_read = self.client.recv(Buffersize)
                        # 如果没有数据传输内容
                        if not bytes_read:
                            break
                        # 读取写入
                        f.write(bytes_read)
                        # 更新进度条
                        progress.update(len(bytes_read))


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
    save_path = '/home/dell/workspace/tmp'
    r()
