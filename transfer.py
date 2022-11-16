import socket
import threading
from threading import Thread

from PyQt5.QtCore import QThread, pyqtSignal

from tools import *


class RecvThread(Thread):
    def __init__(self, client, addr):
        super().__init__()
        self.client = client
        self.addr = addr

    def run(self):
        while True:
            content = self.client.recv(1024).decode('utf-8')

            if content:
                print(f'{self.addr} recv {content}')
            else:
                print(f'{self.addr} disconnect')
                self.client.close()
                break


class TransferThread(QThread):
    trigger_in = pyqtSignal(dict)
    trigger_out = pyqtSignal(dict)

    def __init__(self):
        super(TransferThread, self).__init__()

        self.client = socket.socket()
        self.server = socket.socket()

        self.connected = False
        self.connections = []

    def recv(self, client, addr):
        while True:
            content = client.recv(1024).decode('utf-8')

            if content:
                print(f'{addr} recv {content}')
            else:
                print(f'{addr} disconnect')
                client.close()
                break

    def run(self):
        self.server.bind(('0.0.0.0', 8900))
        self.server.listen(32)

        while True:
            client, address = self.server.accept()
            print(f'{address} connected')
            # signal = {
            #     'type': 'connect',
            #     'address': address
            # }
            # self.child_thread_trigger.emit(signal)

            # p = threading.Thread(target=self.recv, args=(client, address))
            p = RecvThread(client, address)
            p.start()

    def __del__(self):
        self.client.close()
        self.server.close()


if __name__ == '__main__':
    # t = Transfer()
    # t.accept()

    t = TransferThread()
    t.start()

    print('s')
    t.exec()
