import os
import re
import random

def random_date():
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # 为了简单起见，确保日期在每个月的范围内
    return f"{month:02d}-{day:02d}"

def update_date_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 查找并替换日期
    new_date = random_date()
    new_content = re.sub(r"date: (\d{4})-\d{2}-\d{2}", fr"date: \1-{new_date}", content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

def update_dates_in_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            
            if file_name.endswith('.md'):
                print(file_name)
                file_path = os.path.join(root, file_name)
                update_date_in_file(file_path)

# 使用示例
directory_path = 'D:\资料\研一\项目\遥感大模型综述\github\IRIP-BUAA.github.io\_posts'
update_dates_in_directory(directory_path)
