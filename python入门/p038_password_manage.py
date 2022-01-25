"""
p038:个人密码管理器
"""
import sys
import json
import os
import string
import random

password_file = "p038_my_password.txt"
password_dict = {}


def get_password_dict():
    if os.path.isfile(password_file):
        with open(password_file, encoding="utf-8") as fin:
            return json.loads(fin.read())
    else:
        return {}


def show_password():
    password_dict = get_password_dict()
    for key, value in password_dict.items():
        print(f"网站：{key}, 密码:{value}")




def get_new_password(pwd_length=15):
    chars = list(string.ascii_letters +string.digits + string.punctuation)
    random.shuffle(chars)
    return ''.join(chars[:pwd_length])


def add_password(website):
    password_dict = get_password_dict()
    password_dict[website] = get_new_password()
    with open(password_file, mode="w", encoding="utf-8") as fout:
        fout.write(json.dumps(password_dict))



if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) == 2 and sys.argv[1] == "show":
        show_password()

    if len(sys.argv) == 3 and sys.argv[1] == "add":
        add_password(sys.argv[2])