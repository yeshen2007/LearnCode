"""
计算列表和
"""


def sum_of_list(p_list):
    total = 0
    for item in p_list:
        total += item
    return total


if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    print(f"{list1}的和为：", sum_of_list(list1))
    list2 = [17, 5, 3, 5]
    print(f"{list2}的和为：", sum_of_list(list2))