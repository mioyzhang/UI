import random
import math
import socket

# signal type
SIGNAL_TEST = 0
SIGNAL_CHECK = 1
SIGNAL_SEND = 2

OUT_INFO = 3
OUT_SEND = 4
OUT_RECV = 5
OUT_ERROR = 6

# status
TEST_DELAY = 1
TEST_DELAY_FAIL = 2
OTHER_TEST_DELAY = 20

SEND_ERROR = 3
SEND_SUCCESS = 4
RECV_SUCCESS = 5
RECV_ERROR = 6

INIT_ACCEPT_SUCCESS = 7
ACCEPT_ERROR = 8
RECV_CONNECTION = 9
RECV_MESSAGE = 10

TRANSFER_READY = 11
TRANSFER_FINISH = 12

# packet type
PACKET_TEST = 10
PACKET_LINK = 11
PACKET_LINK_BACK = 12

PACKET_UNSENT = -1
PACKET_NONE = 0
PACKET_DETECT = 1
PACKET_ORDER = 2
PACKET_REPLY = 3

PACKET_BACK = 4
PACKET_FILE = 5
PACKET_IMG = 6
PACKET_TOOL = 7

# node type
NODE_NONE = 0
NODE_CENTER = 1
NODE_SHOOTER = 2
NODE_SENSOR = 3
NODE_DRONE = 4
NODE_AIRPLANE = 5
NODE_CAR = 6
NODE_SHIP = 7

NODE_TYPE = [
    '节点',
    '控制中心',
    '射手',
    '传感器',
    '无人机',
    '飞机',
    '车辆',
    '船舶'
]


RX = 0
TX = 1
TIMEOUT = 5

LISTENING_PORT = 8900
LISTENING_PORT_1 = 8901

BUFFER_SIZE = 2048 * 10


IMG_PATH = '/home/dell/workspace/UI/resource/icon'
FILE_PATH = '/home/dell/workspace/UI/resource/file'
SAVE_PATH = '/home/dell/workspace/UI/resource/tmp'

# IMG_PATH = 'D:/Develop/PycharmProjects/UI/resource/icon'
# FILE_PATH = 'D:/Develop/PycharmProjects/UI/resource/file'
# SAVE_PATH = 'D:/Develop/PycharmProjects/UI/resource/tmp'

HostName = socket.gethostname()
# socket.setdefaulttimeout(TIMEOUT)


def generate_random_gps(base_log=120.7, base_lat=30, radius=1000000):
    """
    以(base_log, base_lat)为中心，radius为半径，生成随机GPS信息
    120.7 30为中国的中心位置
    :param base_log:
    :param base_lat:
    :param radius:
    :return:
    """
    radius_in_degrees = radius / 111300
    u = float(random.uniform(0.0, 1.0))
    v = float(random.uniform(0.0, 1.0))
    w = radius_in_degrees * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    y = w * math.sin(t)
    longitude = y + base_log
    latitude = x + base_lat
    return round(longitude, 6), round(latitude, 6)


def extract_address(s, default_port=LISTENING_PORT):
    """
    判断ip地址合法性
    :param s:
    :param default_port:
    :return:
    """
    def is_ip(str_):
        import re
        compile_ip = re.compile(r'^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
        if compile_ip.match(str_):
            return True
        else:
            return False

    if ':' in s:
        s = s.split(':')
        if len(s) != 2:
            return False
        else:
            ip, port = s
            if is_ip(ip) and port.isdigit():
                return ip, int(port)
            else:
                return False
    else:
        if is_ip(s):
            return s, default_port
        else:
            return False
