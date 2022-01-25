"""
p021:统计学生爱好的人数
"""
if __name__ == '__main__':
    like_count = {}

    with open("p021_student_like.txt", encoding="utf-8") as fp:
        for line in fp:
            line = line[:-1]
            sname, likes = line.split()
            like_list = likes.split(",")
            for like in like_list:
                if like not in like_count:
                    like_count[like] = 0
                like_count[like] += 1

    print(like_count)