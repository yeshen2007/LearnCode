#python自动生成excel数据文件
# Faker pandas openpyxl需要安装
import random
from faker import Faker
import pandas as pd
import os

fake = Faker("zh_CN")

def auto_gen_excel(file_path,file_n):
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    for i in range(file_n):
        nn = random.randint(3, 10)
        names = [fake.name() for _ in range(nn)]
        grades = [random.randint(50, 100) for _ in range(nn)]
        d = {'姓名': names, '考试分数': grades}
        file = os.path.join(file_path, f'班级{i+1}.xlsx')
        pd.DataFrame(d).to_excel(file, index=False)
    print("Done")

if __name__ == '__main__':
    auto_gen_excel('excel', 5)