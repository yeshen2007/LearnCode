"""
p007:给Series添加元素
"""

import pandas as pd

grades = {"语文": 80, "数学": 85, "英语": 90, "计算机": 95, "体育": 100}
data = pd.Series(data=grades)

data = data.append(pd.Series({"物理": 88, "化学": 89}))
print(data)