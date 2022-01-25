"""
p022:获取当前的日期时间
"""

import datetime

if __name__ == '__main__':
    curr_datetime = datetime.datetime.now()
    print(curr_datetime, type(curr_datetime))
    str_time = curr_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print("str_time:", str_time)
    print("year:", curr_datetime.year)
    print("month:", curr_datetime.month)
    print("day:", curr_datetime.day)
    print("hour:", curr_datetime.hour)
    print("minute:", curr_datetime.minute)
    print("second:", curr_datetime.second)