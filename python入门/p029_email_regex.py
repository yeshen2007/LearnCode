"""
p029: 自动提取邮箱地址
"""
import re

if __name__ == '__main__':
    content = """
    大多数Windows文本文件使用ANSI、OEM或者Unicode编码。Windows
    所指的ANSI编码通常是1字节的ISO-8859编码，不过对于像中文、日文、
    朝鲜文这样的环境，需要使用2字节字符集14555110@qq.com。在过渡至Unicode前，Windows
    一直用ANSI作a12545bcded.com为系统默认的编码。而OEM编码，也是通常所说的MS-DOS代码页，
    是IBM为早期IBM个人电脑的文本abcded@qq.cn模式显示系统定义的。在全屏的MS-DOS程序中
    同时使用了图形的python_abc@sina.comabc.com和按行绘制的字符。新版本的Windows可以使用UTF-16LE和
    UTF-8之类的Unicode编码。
    """


    # verbose,多行编写
    # a-z   A-Z  0-9  _  -  (+至少一个符号)
    # @
    # a-z A-Z 0-9  (+至少一个符号)
    # . (转义)
    # a-z A-Z    {2,4}(最多出现2-4个)
    pattern = re.compile(r"""
    [a-zA-Z0-9_-]+
    @
    [a-zA-Z0-9]+
    \.
    [a-zA-Z]{2,4}
    """, re.VERBOSE
    )

    results = re.findall(pattern, content)
    for email in results:
        print(email)