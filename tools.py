import random
import math
import socket

# type
SIGNAL_TEST = 0
SIGNAL_CHECK = 1
SIGNAL_SEND = 2

OUT_INFO = 3
OUT_SEND = 4
OUT_RECV = 5
OUT_ERROR = 15

# status
TEST_DELAY = 7
TEST_DELAY_FAIL = 6

SEND_ERROR = 8
SEND_SUCCESS = 9
RECV_ERROR = 10

PACKET_UNSENT = -1
PACKET_NONE = 0
PACKET_DETECT = 1
PACKET_ORDER = 2
PACKET_REPLY = 3
PACKET_BACK = 4

PACKET_FILE = 7
PACKET_TEST = 8
PACKET_LINK = 9

PACKET_TOOL = 5

INIT_SUCCESS = 14
RECV_CONNECTION = 11
RECV_MESSAGE = 12

TRANSFER_READY = 17
TRANSFER_FINISH = 18

RX = 0
TX = 1
TIMEOUT = 3
LISTENING_PORT = 8900

BUFFER_SIZE = 2048 * 10


img_path = '/home/dell/workspace/UI/resource/icon'
file_path = '/home/dell/workspace/UI/resource/file'
save_path = '/home/dell/workspace/UI/resource/tmp'

# img_path = 'D:/Develop/PycharmProjects/UI/resource/icon'
# file_path = 'D:/Develop/PycharmProjects/UI/resource/file'
# save_path = 'D:/Develop/PycharmProjects/UI/resource/tmp'

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
    # 这里是想保留6位小数点
    # loga = '%.6f' % longitude
    # lata = '%.6f' % latitude
    # return loga, lata
    return longitude, latitude
