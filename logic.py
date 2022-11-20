import json

from tools import *


class Node(object):

    def __init__(self, label=None, ip_address=None, port=None, mac_address=None):
        super(Node, self).__init__()
        self.label = label
        self.ip_address = ip_address
        self.port = port
        self.mac_address = mac_address

        self.type = None
        self.status = None
        self.last_seen = None
        self.last_gps = None

    def __str__(self):
        return f'Node({self.ip_address}:{self.port})'

    def __repr__(self):
        return f'Node({self.ip_address}:{self.port})'

    def __hash__(self) -> int:
        return hash(self.ip_address) ^ hash(self.port)

    def __eq__(self, other):
        return isinstance(other, Node) and self.ip_address == other.ip_address and self.port == other.port


class Message(object):
    def __init__(self, args):
        super(Message, self).__init__()
        if type(args) not in (str, dict):
            raise TypeError
        if isinstance(args, str):
            args = json.loads(args)

        self.sequence = args.get('sequence')
        self.type = args.get('type')
        self.with_gps = args.get('with_gps')
        self.gps = args.get('gps')
        self.content = args.get('content')
        self.files = args.get('files')
        self.images = args.get('images')
    
    def to_dict(self, with_path=True):
        files = self.files if with_path else [i.split('/')[-1] for i in self.files]
        images = self.images if with_path else [i.split('/')[-1] for i in self.images]

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

    def summary(self):
        return self.content[:20] if len(self.content) > 20 else self.content

    def __hash__(self) -> int:
        return self.sequence

    def __eq__(self, other):
        return isinstance(other, Message) and self.sequence == other.sequence

    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=4, ensure_ascii=False)
    
    def __repr__(self) -> str:
        return f'Message({self.sequence})'


class Packet(object):
    def __init__(self, message, src=None, dst=None, protocol=None, recv_time=None, send_time=None, flow=None):
        super().__init__()
        
        self.src = src
        self.dst = dst
        self.protocol = protocol
        self.status = PACKET_UNSENT
        self.recv_time = recv_time
        self.send_time = send_time
        self.flow = flow

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
    # print([p])
    a = Node(ip_address='10.0.0.1', port=123)
    b = Node(ip_address='10.0.0.1', port=124)
    print(a)
    print(b)
    print(a == b)
    # print(hash(a))
    # print(hash(b))
    print(a in [a, b])
    print(a in [b])
    print(Node(ip_address='10.0.0.1', port=123) in [a, b])
