"""
p026: unix时间戳转换为日期格式
"""

import datetime

if __name__ == '__main__':
    unix_time = 1620747647
    datetime_obj = datetime.datetime.fromtimestamp(unix_time)
    datetime_str = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
    print(datetime_str)