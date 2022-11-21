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


import random

s = random.randint(0, 10 ** 8 - 1)
print(s)