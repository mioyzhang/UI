from transfer import TransferThread
from tools import *
from logic import Packet, Message


# m = Message({'sequence': 123, 'files': [f'{img_path}/传感器.png']})
# p = Packet(message=m)
# print(p)
#
# c = TransferThread()
# c.test_connect(('127.0.0.1', 8901))
# # c.link_to(('127.0.0.1', LISTENING_PORT))
# c.send_message(m, ('127.0.0.1', 8901))


import string
import random

a = f'{random.choice(string.ascii_uppercase)}{random.randint(0, 99)}'
b = '.'.join([str(random.randint(1, 254)) for _ in range(4)])

print(a)
print(b)

for _ in range(100):
    print(random.randint(0, 7), end=' ')