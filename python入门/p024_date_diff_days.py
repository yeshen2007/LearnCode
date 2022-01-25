"""
p024:计算任意日期7天前的日期
"""
import datetime

def get_diff_days(pdate, days):
    pdate_obj = datetime.datetime.strptime(pdate, "%Y-%m-%d")
    time_gap = datetime.timedelta(days=days)
    pdate_result = pdate_obj - time_gap
    return pdate_result.strftime("%Y-%m-%d")


if __name__ == '__main__':
    pdate = "2022-01-16"
    print(get_diff_days(pdate, 7))