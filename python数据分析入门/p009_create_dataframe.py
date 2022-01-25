"""
p009:创建一个dataframe
提示：给dataframe 传一个字典
"""

import pandas as pd

df = pd.DataFrame(
    {
        "姓名": ["小张", "小王", "小李", "小周"],
        "性别": ["男", "男", "女", "男"],
        "年龄": [19, 18, 20, 40]
    }
)

print(df)
