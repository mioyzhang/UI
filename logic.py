import json


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


class Message(object):
    def __init__(self, sequence=None, type=None, content=None, with_gps=False, gps=None, files=[], images=[]):
        super(Message, self).__init__()
        self.sequence = sequence
        self.type = type
        self.content = content
        self.with_gps = with_gps
        self.gps = gps
        self.files = files
        self.images = images
    
    def to_dict(self):
        message_dict = {
            'sequence': self.sequence,
            'type': self.type,
            'content': self.content,
            'with_gps': self.with_gps,
            'gps': self.gps,
            'files': self.files,
            'images': self.images
        }
        return message_dict

    def to_json(self):
        message_json = json.dumps(self.to_dict())
        return message_json
    
    def __str__(self) -> str:
        return self.to_json()


class Packet(object):
    def __init__(self) -> None:
        super().__init__()
        
        self.message = None
        self.src = None
        self.dst = None


class Logic(object):
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)

    def address_in_nodes(self, address):
        return address in [i.ip_address for i in self.nodes]