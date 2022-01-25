"""
p002:使用pandas将dict变成Series,输出到命令行
"""

import pandas as pd

grades = {"语文": 80, "数学": 85, "英语": 90, "计算机": 95, "体育": 100}
data = pd.Series(data=grades)
print(data)