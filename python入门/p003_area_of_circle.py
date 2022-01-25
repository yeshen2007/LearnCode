"""
计算圆的面积
"""
import math


def compute_area_of_circle(r):
    return round(math.pi * r * r, 2)


if __name__ == '__main__':
    r = 9
    print(f"r = {r}, s = {compute_area_of_circle(r)}")
