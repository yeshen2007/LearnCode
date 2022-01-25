"""
p030: 验证用户名密码是否合规

写一个函数，验证密码是否满足条件
1.长度位于6-20之间
2.必须包含至少1个小写字母
3.必须包含至少1个大写字母
4.必须包含至少1个数字
5.必须包含至少1个特殊字符
"""

import re

def check_password(password):
    if not 6 <= len(password) <= 20:
        return False, "密码必须在6-20之间"
    if not re.findall(r"[a-z]", password):
        return False, "必须包含至少1个小写字母"
    if not re.findall(r"[A-Z]", password):
        return False, "必须包含至少1个大写字母"
    if not re.findall(r"[0-9]", password):
        return False, "必须包含至少1个数字"
    if not re.findall(r"[^a-zA-Z0-9]", password):
        return False, "必须包含至少1个特殊字符"
    return True, None


password1 = "zZ12345678@"
print(check_password(password1))

password2 = "Z12345678@"
print(check_password(password2))

password3 = "z12345678@"
print(check_password(password3))

password4 = "zZSDFSDF@"
print(check_password(password4))

password5 = "zZ12345678"
print(check_password(password5))

password5 = "zZ12@"
print(check_password(password5))



