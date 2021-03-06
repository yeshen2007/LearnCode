"""
p032: 给文章手机号打马赛克效果
"""
import re

if __name__ == '__main__':

    content = """
    青春23是什么，每个人都有12345678自己的见解。我们只是爱借523645着青2342春的名义再13953652564肆无忌惮一次，用时光绘22342画着未
    来的颜色，用汗水打造13987456985着56456理想的殿堂，用岁月承载134569525365着曾经的梦想，再将他们一一打磨，雕刻成最美丽123456952
    65478的模样。我们只是想14425这青葱的岁月，留下些2342回忆，这样的回忆，是能够让13777777777我们在多年之后笑着流泪，说，我不曾后悔。
    """

    pattern = r"(1[3-9])\d{9}"

    print(re.sub(pattern, r"\1******", content))  # \1   第一个括号的内容