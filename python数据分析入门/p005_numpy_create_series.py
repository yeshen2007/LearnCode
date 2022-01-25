"""
p005:用numpy创建series
"""
import pandas as pd
import numpy as np


s = pd.Series(
    # 数值：10~90，间隔10
    np.arange(10, 100, 10),

    # 索引：101~109，间隔1
    index=np.arange(101, 110),

    # 类型：float
    dtype='float'
)
print(s)