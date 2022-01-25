"""
实现列表的去重
"""

def get_unique_list(lista):
    result = []
    for item in lista:
        if item not in result:
            result.append(item)
    return result


if __name__ == '__main__':
    lista = [10, 20, 30, 10, 20]
    # 第一种方法
    print(f"source list :{lista}, unique list : ", get_unique_list(lista))

    # 第二种方法
    print(f"source list :{lista}, unique list : ", list(set(lista)))