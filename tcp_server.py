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

                if content:
                    print(f'{self.addr} recv {content}')
                else:
                    print(f'{self.addr} disconnect')
                    self.client.close()
                    break

                info = json.loads(content)
                if info.get('type') == 'test':
                    print(f'{self.addr} send {content}')
                    self.client.send(content.encode())
            except BaseException as e:
                print(e)
                exit()


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
    r()
