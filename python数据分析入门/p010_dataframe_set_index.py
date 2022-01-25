"""
p010:给dataframe设定索引列
"""
import pandas as pd

data = {
        "姓名": ["小张", "小王", "小李", "小周"],
        "性别": ["男", "男", "女", "男"],
        "年龄": [19, 18, 20, 40]
    }
df = pd.DataFrame(data)


df.set_index('姓名', inplace=True)
print(df)