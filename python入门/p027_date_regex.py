"""
p027:正则表达式，验证字符串是不是日期
"""

import re
def date_is_right(date):
    return re.match("\d{4}-\d{2}-\d{2}", date) is not None


date1 = "2022-01-16"
print(date_is_right(date1))

date2 = "202-01-16"
print(date_is_right(date2))

date3 = "2022/01-16"
print(date_is_right(date3))

date4 = "20220116"
print(date_is_right(date4))

date5 = "202a-01-16"
print(date_is_right(date5))