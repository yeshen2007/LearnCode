"""
数字的阶乘
"""


def get_jiecheng(number):
    result = 1
    while number > 0:
        result *= number
        number -= 1
    return result


if __name__ == '__main__':
    number = 20
    print(f"{number}! = {get_jiecheng(number)}")
