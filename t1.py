from transfer import TransferThread
from tools import *
from logic import Packet, Message



m = Message({'sequence': 123, 'files': ['/home/dell/workspace/UI/resource/icon/传感器.png']})
p = Packet(message=m)
print(p)

c = TransferThread()
# # c.test_connect(('127.0.0.1', LISTENING_PORT))
# c.link_to(('127.0.0.1', LISTENING_PORT))
c.send_message(p, ('127.0.0.1', LISTENING_PORT))


