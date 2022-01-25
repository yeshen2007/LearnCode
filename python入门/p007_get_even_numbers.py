"""
显示范围内所有的偶数，不包含结束值
"""


def get_even_numbers(begin, end):
    result = []
    for item in range(begin, end):
        if item % 2 == 0:
            result.append(item)
    return result


if __name__ == '__main__':
    begin = 10
    end = 25

    # 第一种方法
    print(f"begin = {begin}, end = {end}, even numbers: ", get_even_numbers(begin, end))

    # 第二种方法
    print(f"begin = {begin}, end = {end}, even numbers: ", [item for item in range(begin, end) if item % 2 == 0])
