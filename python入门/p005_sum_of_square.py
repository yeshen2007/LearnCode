"""
计算前n个数字的平方和
"""


def sum_of_square(n):
    result = 0
    for number in range(1, n+1):
        result += number ** 2
    return result


if __name__ == '__main__':
    n = 10
    print(f"前{n}的平方和: ", sum_of_square(n))