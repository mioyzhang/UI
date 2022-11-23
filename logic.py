import os
import json
import string
import random
import time

import faker
faker = faker.Faker()

from tools import *


class Node(object):

    def __init__(self, label=None, ip_address=None, port=None, type_=NODE_NONE, last_seen=None, generate=False):
        super(Node, self).__init__()
        self.label = label
        self.ip_address = ip_address
        self.port = port    # udp listen port

        self.last_seen = last_seen
        self.type = type_
        self.status = None
        self.last_gps = None
        self.packets = []

        if generate:
            self.label = f'{random.choice(string.ascii_uppercase)}{random.randint(0, 99)}'
            self.ip_address = '.'.join([str(random.randint(1, 254)) for _ in range(4)])
            self.last_seen = time.time() - random.randint(0, 10000)
            self.type = random.randint(0, 7)

    def update(self, node):
        if not isinstance(node, Node):
            return

        if not self.label and node.label:
            self.label = node.label
        if node.last_seen:
            if not self.last_seen:
                self.last_seen = node.last_seen
            if self.last_seen and node.last_seen > self.last_seen:
                self.last_seen = node.last_seen

    def __str__(self):
        return f'{self.label}({self.ip_address})'

    def __repr__(self):
        return f'Node({self.label} {self.ip_address})'

    def __hash__(self) -> int:
        return hash(self.ip_address)

    def __eq__(self, other):
        return isinstance(other, Node) and self.ip_address == other.ip_address


class Message(object):
    def __init__(self, args):
        super(Message, self).__init__()
        if type(args) in (str, dict):
            if isinstance(args, str):
                args = json.loads(args)
            self.sequence = args.get('sequence')
            self.type = args.get('type')
            self.with_gps = args.get('with_gps')
            self.gps = args.get('gps')
            self.content = args.get('content')
            self.files = args.get('files') if args.get('files') else []
            self.images = args.get('images') if args.get('images') else []
        else:
            self.sequence = random.randint(0, 10 ** 8 - 1)
            self.type = random.randint(0, 3)
            self.with_gps = random.choice([True, False])
            self.gps =  generate_random_gps()
            self.content =  faker.text()

            imgs = os.listdir(IMG_PATH)
            imgs = random.sample(imgs, random.randint(0, len(imgs)))
            imgs = [os.path.join(IMG_PATH, i) for i in imgs]

            files = os.listdir(FILE_PATH)
            files = random.sample(files, random.randint(0, len(files)))
            files = [os.path.join(FILE_PATH, i) for i in files]

            self.files = files
            self.images = imgs

    def to_dict(self, with_path=True):
        files = self.files if with_path else [os.path.basename(i) for i in self.files]
        images = self.images if with_path else [os.path.basename(i) for i in self.images]

        message_dict = {
            'sequence': self.sequence,
            'type': self.type,
            'content': self.content,
            'with_gps': self.with_gps,
            'gps': self.gps,
            'files': files,
            'images': images
        }
        return message_dict

    def to_json(self, with_path=True):
        return json.dumps(self.to_dict(with_path), ensure_ascii=False)

    def summary(self, length=30):
        return self.content[:length] if len(self.content) > length else self.content

    def detail(self):
        return json.dumps(self.to_dict(), indent=4, ensure_ascii=False)

    def __hash__(self) -> int:
        return self.sequence

    def __eq__(self, other):
        return isinstance(other, Message) and self.sequence == other.sequence

    def __str__(self) -> str:
        return f'Message({self.sequence})'
    
    def __repr__(self) -> str:
        return f'Message({self.sequence})'


class Packet(object):
    def __init__(self, message, src=None, dst=None, protocol=None, time_=None, send_time=None, flow=None, status=1, generate=False):
        super().__init__()
        
        self.src = src
        self.dst = dst
        self.protocol = protocol
        self.time = time_
        self.flow = flow
        self.status = status

        self.message = message
        self.sequence = self.message.sequence

        if generate:
            self.flow = random.randint(0, 1)
            if self.flow == RX:
                self.src = '.'.join([str(random.randint(1, 254)) for _ in range(4)])
                self.dst = None
            if self.flow == TX:
                self.src = None
                self.dst = '.'.join([str(random.randint(1, 254)) for _ in range(4)])

            self.protocol = protocol
            self.recv_time = recv_time
            self.send_time = send_time
            self.status = random.randint(0, 1)
            self.message = message
            self.sequence = self.message.sequence

    def to_dict(self):
        packet_dict = {
            'src': self.src,
            'dst': self.dst,
            'protocol': self.protocol,
            'status': self.status,
            'recv_time': self.recv_time,
            'send_time': self.send_time,
            'message': self.message.to_dict()
        }
        return packet_dict

    def to_json(self):
        return json.dumps(self.to_dict(), ensure_ascii=False)

    def __hash__(self) -> int:
        return self.sequence

    def __eq__(self, other):
        return isinstance(other, Packet) and self.sequence == other.sequence
    
    def __str__(self) -> str:
        # return json.dumps(self.to_dict(), indent=4, ensure_ascii=False)
        return f'Packet({self.message.sequence})'
    
    def __repr__(self) -> str:
        return f'Packet({self.message.sequence})'


if __name__ == '__main__':
    # m = Message({})
    # print(m)
    # print([m])
    #
    # p = Packet(m)
    # print(p)
    for _ in range(10):
        print(Message(None))
    
    print(Message(None).detail())