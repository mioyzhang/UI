import json

from tools import *


class Node(object):

    def __init__(self, label=None, ip_address=None, mac_address=None):
        super(Node, self).__init__()
        self.label = label
        self.ip_address = ip_address
        self.mac_address = mac_address

        self.type = None
        self.status = None
        self.last_seen = None
        self.last_gps = None

    def __str__(self):
        return f'Node({self.label})'

    def __hash__(self) -> int:
        return hash(self.ip_address)

    def __eq__(self, other):
        return isinstance(other, Node) and self.ip_address == other.ip_address


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
    
    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=4, ensure_ascii=False)
    
    def __repr__(self) -> str:
        return f'Message({self.sequence})'


class Packet(object):
    def __init__(self, message, src=None, dst=None, protocol='TCP'):
        super().__init__()
        
        self.src = src
        self.dst = dst
        self.protocol = protocol
        self.status = PACKET_UNSENT
        self.recv_time = None
        self.send_time = None

        self.message = message

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
    
    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=4, ensure_ascii=False)
    
    def __repr__(self) -> str:
        return f'Packet({self.message.sequence})'


class Logic(object):
    def __init__(self):
        self.nodes = []
        self.messages = []
        self.packets = []

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)

    def address_in_nodes(self, address):
        return address in [i.ip_address for i in self.nodes]


if __name__ == '__main__':
    m = Message({})
    print(m)
    print([m])

    p = Packet(m)
    print(p)
    print([p])
