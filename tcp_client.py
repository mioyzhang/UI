import socket  # 导入 socket 模块

s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 8900  # 设置端口号

s.connect((host, port))
while True:
    msg = input('send:')
    s.send(msg.encode())

