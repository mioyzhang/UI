import random
import math


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
    loga = '%.6f' % longitude
    lata = '%.6f' % latitude
    return loga, lata