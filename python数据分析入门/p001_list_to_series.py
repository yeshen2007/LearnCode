"""
p001:使用pandas将list变成Series,输出到命令行
"""

import pandas as pd

cousers = ["语文", "数学", "英语", "计算机", "体育"]
data = pd.Series(data=cousers)
print(data)