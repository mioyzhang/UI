import socket  # 导入 socket 模块
import json
import os

from tools import *

s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 8900  # 设置端口号
Buffersize = 4096*10

try:
    # s.connect((host, port))
    s.connect(('127.0.0.1', port))
except BaseException as e:
    raise e

# while True:
#     msg = input('send:')
#     s.send(msg.encode())


file = 'D:/Develop/PycharmProjects/UI/resource/file/1.txt'

m = {
    'type': PACKET_FILE,
    'file_name': file.split('/')[-1],
    'file_size': os.path.getsize(file)
}
m = json.dumps(m)

# s.send(m.encode())
# print(f'send {m}')
# r = s.recv(2048)
# print(r)
# r = s.recv(2048)
# print(r)

# with open(file, 'rb') as f:
#     # 读取文件
#     while True:
#         bytes_read = f.read(Buffersize)
#         if not bytes_read:
#             break
#         # sendall 确保网络忙碌的时候，数据仍然可以传输
#         s.sendall(bytes_read)
#
# s.close()