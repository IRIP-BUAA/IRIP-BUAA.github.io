import pandas as pd
from datetime import datetime

# 读取Excel文件中的所有表
excel_file = '大模型数据集.xlsx'
sheets = pd.read_excel(excel_file, sheet_name=None)

# 处理每个表
for sheet_name, df in sheets.items():
    for index, row in df.iterrows():
        title = row['数据集名称']
        date = row['发布时间']
        date_formatted = f"{date}-01-01 00:00:00 +0800"  # 自动补全为 YYYY-01-01 00:00:00 +0800 的格式
        md_content = f"""---
title: {title}
author: Zack
date: {date_formatted}
categories: [{row['任务']}]
tags: [dataset, {row['模态']}]
math: true
pin: false
---

- 数据集名称: {row['数据集名称']}
- 任务: {row['任务']}
- 发布时间: {row['发布时间']}
- 模态: {row['模态']}
- 数量: {row['数量']}
- 代码源链接: {row['代码源链接']}
- 论文源链接: {row['论文源链接']}
- 详细描述: {row['详细描述']}
"""

        # 将Markdown内容写入文件
        md_filename = date_formatted.split(' ')[0] +'-'+ row['数据集名称'] + '.md'
        with open(md_filename, 'w', encoding='utf-8') as file:
            file.write(md_content)

        print(f"{md_filename} has been created.")
        break
    break