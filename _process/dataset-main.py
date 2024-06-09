import pandas as pd
from datetime import datetime
import re

def sanitize_filename(input_string, max_length=255):
    # 删除非法字符
    sanitized_string = re.sub(r'[\/:*?"<>|]', '', input_string)
    # 替换特殊字符
    sanitized_string = sanitized_string.replace(':', '-')
    # 处理空格（根据需要可以选择不同的处理方式）
    # sanitized_string = sanitized_string.replace(' ', '_')
    # 截断文件名（确保总长度不超过指定最大长度）
    sanitized_string = sanitized_string[:max_length]
    return sanitized_string

# 读取Excel文件中的所有表
excel_file = '大模型数据集.xlsx'
sheets = pd.read_excel(excel_file, sheet_name=None)

# 处理每个表
for sheet_name, df in sheets.items():
    for index, row in df.iterrows():
        title = sanitize_filename(row['数据集名称'])
        date = row['发布时间']
        date_formatted = f"{date}-01-01 00:00:00 +0800" if not pd.isna(date) else ""

        md_content = f"""---
title: {title}
author: Zack
date: {date_formatted}
categories: [{sheet_name}]
tags: [dataset, {row['模态']}]
math: true
pin: false
---
"""

        if not pd.isna(row['数据集名称']):
            md_content += f"- 数据集名称: {row['数据集名称']}\n"
        if not pd.isna(row['任务']):
            md_content += f"- 任务: {row['任务']}\n"
        if not pd.isna(row['发布时间']):
            md_content += f"- 发布时间: {row['发布时间']}\n"
        if not pd.isna(row['模态']):
            md_content += f"- 模态: {row['模态']}\n"
        if not pd.isna(row['数量']):
            md_content += f"- 数量: {row['数量']}\n"
        if not pd.isna(row['代码源链接']):
            md_content += f"- 代码源链接: {row['代码源链接']}\n"
        if not pd.isna(row['论文源链接']):
            md_content += f"- 论文源链接: {row['论文源链接']}\n"
        if not pd.isna(row['详细描述']):
            md_content += f"- 详细描述: {row['详细描述']}\n"

        # 将Markdown内容写入文件
        md_filename = '../_posts/' + date_formatted.split(' ')[0] +'-'+ sanitize_filename(row['数据集名称']) + '.md'
        with open(md_filename, 'w', encoding='utf-8') as file:
            file.write(md_content)

        print(f"{md_filename} has been created.")
      
  