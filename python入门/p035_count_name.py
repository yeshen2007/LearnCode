"""
p035:统计一本小说的人名
"""
import jieba.posseg as posseg
import pandas as pd

if __name__ == '__main__':
    # content = """李明喜欢韩梅梅，他俩早恋了"""
    with open("p035_鹿鼎记.txt", encoding="GBK", errors="ignore") as fp:
        content = fp.read()
    # print(content)

    names = []
    for word, flag in list(posseg.cut(content)):
        if flag == "nr":
            names.append(word)
            # print(word, flag)

    print(pd.Series(names).value_counts()[:10])