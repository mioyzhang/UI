#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Project : pypj
# @File    : arp_scan.py
# @IDE     : PyCharm
# @Author  : zhang bin
# @Date    : 2022/2/17 16:30:53
# @DES     : 
"""
import sys
import netifaces
from scapy.all import srp, sr1, Ether, ARP, IP, ICMP
# from scapy.all import *
from netifaces import AF_INET

TIMEOUT = 2


def get_interface_ip_address(iface, with_mask=True):
    info = netifaces.ifaddresses(iface)
    if AF_INET not in info.keys():
        return None
    info = info[AF_INET][0]
    if with_mask:
        mask = ''.join([str(bin(int(i)))[2:] for i in info['netmask'].split('.')]).count('1')
        return info['addr'] + '/' + str(mask)
    else:
        return info['addr']


def get_interface_mac_address(iface):
    info = netifaces.ifaddresses(iface)
    if 17 not in info.keys():
        return None
    return info[17][0]['addr']


def arp_scan(iface, ip_scan):
    '''
    需要权限
    '''
    print('scan {} {}...'.format(iface, ip_scan))
    # ip_scan = get_interface_ip_address(iface)
    src = get_interface_mac_address(iface)

    try:
        ans, unans = srp(Ether(dst='FF:FF:FF:FF:FF:FF', src=src)/ARP(pdst=ip_scan), iface=iface, timeout=2, verbose=False)

    except Exception as e:
        raise  e

    else:
        arp_table = {rcv.sprintf('%ARP.psrc%'): rcv.sprintf('%Ether.src%') for _, rcv in ans}
        return arp_table


def ping(ip):
    packet = IP(dst=ip, ttl=20)/ICMP()
    reply = sr1(packet, timeout=TIMEOUT, verbose=False)
    if reply is None:
        return 0
    else:
        return 1


if __name__ == '__main__':
    print(get_interface_mac_address('enp0s31f6'))
    print(get_interface_ip_address('enp0s31f6'))

    s = arp_scan('enp0s31f6', '192.168.0.0/24')
    import socket

    for i, j in s.items():
        print(i, j)
        print(socket.gethostbyaddr(i))