"""
p023:计算自己活了多少天
"""
import datetime
if __name__ == '__main__':
    birthday = '1997-12-21'
    birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d")
    print(birthday_date)

    current_datetime = datetime.datetime.now()
    print(current_datetime)

    minus_datetime = current_datetime - birthday_date
    print(minus_datetime)

    print("days:", minus_datetime.days)