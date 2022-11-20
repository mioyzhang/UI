from transfer import TransferThread
from tools import *
from logic import Packet, Message



m = Message({})
p = Packet(message=m)
print(p)

c = TransferThread()
# # c.test_connect(('127.0.0.1', LISTENING_PORT))
# c.link_to(('127.0.0.1', LISTENING_PORT))
c.send_packet(p, ('127.0.0.1', LISTENING_PORT))


