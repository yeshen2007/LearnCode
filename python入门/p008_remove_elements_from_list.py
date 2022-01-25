"""
移除列表中的多个元素
"""

def remove_elements_from_list(lista, listb):
    for item in listb:
        lista.remove(item)
    return lista


if __name__ == '__main__':
    lista = [3, 5, 7, 9, 11, 13]
    listb = [7, 11]

    # 第一种方法
    print(f"from {lista} remove {listb}, result : ", remove_elements_from_list(lista, listb))

    lista = [3, 5, 7, 9, 11, 13]
    listb = [7, 11]
    # 第二种方法
    print(f"from {lista} remove {listb}, result : ", [item for item in lista if item not in listb])