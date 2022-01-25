"""
对简单列表的排序
"""
if __name__ == '__main__':
    lista = [20, 40, 30, 50, 10]
    # lista.sort()   # 原地排序
    # lista.sort(reverse=True)   # 原地排序
    print("lista is ", lista)

    # 默认升序排列
    listb = sorted(lista)
    print("listb is ", listb)

    # 降序排列
    listc = sorted(lista, reverse=True)
    print("listc is ", listc)
