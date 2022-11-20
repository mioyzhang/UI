import socket
# 客户端
def main():
    # 1,创建udp类型的socket
    udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2，指定目的地址（ip和端口号
    serverAddr = ('127.0.0.1', 8080)
    while True:
        # 3，发送数据
        sendData = input("客户端！请输入请求数据：")
        udpSocket.sendto(sendData.encode(), serverAddr)
        # 4，接收数据是一个元组,本次接收数据的最大长度，建议是2^xxx次方
        receData, peerAddr = udpSocket.recvfrom(1024)
        print(receData.decode())
        # print(peerAddr)
    # 5,关闭socket
    udpSocket.close()

if __name__ == '__main__':
    main()