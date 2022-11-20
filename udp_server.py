#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : xiaoke
import socket
# 服务端
def main():
    # 1,创建数据报套接字
    udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2，绑定本地地址，核心是为绑定并公布端口
    # ''表示指定任意ip：0.0.0.0，系统中任意ip的数据都可以接收
    myAddr = ('', 8080)
    udpSocket.bind(myAddr)
    # 3，接收客户端数据，获得客户端的地址（ip和端口号）
    recData, clientAddr = udpSocket.recvfrom(1024)
    print(clientAddr)
    print(recData.decode())
    # 4，回复客户端消息
    udpSocket.sendto(recData, clientAddr)
    # 5，关闭socket
    udpSocket.close()

if __name__ == '__main__':
    main()