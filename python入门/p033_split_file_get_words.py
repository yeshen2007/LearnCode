"""
p033: 实现英文分词计算词频
"""

import re
import pandas as pd

if __name__ == '__main__':
    with open("p033_english_file.txt", encoding="utf-8") as fp:
        content = fp.read()

    # print(content)
    # print(content.split())

    words = re.split(r"[\s.()-?]+", content)
    print(pd.Series(words).value_counts()[:20])