"""
p012:读取文件实现排序
"""
def read_file():
    reulst = []
    with open("p012_student_grade.txt", encoding="utf-8") as fp:
        for line in fp:
            line = line[:-1]
            line = line.split(",")
            line[2] = int(line[2])
            reulst.append(line)
    return reulst

def sort_grades(datas):
    result = sorted(datas, key=lambda x: x[2])
    return result

def wirte_file(datas):
    with open("p012_student_grade2.txt", mode="w", encoding="utf-8") as fp:
        for item in datas:
            item[2] = str(item[2])
            line = ','.join(item) + "\n"
            fp.write(line)


if __name__ == '__main__':
    # 读取文件
    datas = read_file()
    print(datas)

    # 排序数据
    datas = sort_grades(datas)
    print(datas)

    # 写入文件
    wirte_file(datas)


