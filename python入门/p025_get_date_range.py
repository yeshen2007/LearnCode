"""
p025:获取开始到结束的所有日期
"""

import datetime

def get_date_range(begin_date, end_date):
    date_list = []
    while begin_date <= end_date:
        date_list.append(begin_date)
        begin_date_obj = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
        days1_timedate = datetime.timedelta(days=1)
        begin_date = (begin_date_obj + days1_timedate).strftime("%Y-%m-%d")

    return date_list


if __name__ == '__main__':
    begin_date = "2021-04-28"
    end_date = "2021-05-03"

    date_list = get_date_range(begin_date, end_date)
    print(date_list)