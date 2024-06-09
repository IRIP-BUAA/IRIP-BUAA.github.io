import pandas as pd
from datetime import datetime

# 读取Excel文件中的所有表
excel_file = '遥感大模型论文1.xlsx'
sheets = pd.read_excel(excel_file, sheet_name=None)

# 处理每个表
for sheet_name, df in sheets.items():
    for index, row in df.iterrows():
        title = row['Paper']
        date = row['Published in'].split(' ')[-1]
        date_formatted = f"{date}-01-01 00:00:00 +0800" if not pd.isna(date) else ""

        md_content = f"""---
title: {title}
author: Zack
date: {date_formatted}
categories: [{row['Published in'].split(' ')[0]}]
tags: [paper, {row['Tag']}]
math: true
pin: false
---
"""

        if not pd.isna(row['Paper']):
            md_content += f"- 论文名称: {row['Paper']}\n"
        if not pd.isna(row['Tag']):
            md_content += f"- 模型架构: {row['Tag']}\n"
        if not pd.isna(row['Visual Encoder']):
            md_content += f"- Visual Encoder: {row['Visual Encoder']}\n"
        if not pd.isna(row['Text Encoder']):
            md_content += f"- Text Encoder: {row['Text Encoder']}\n"
        if not pd.isna(row['Model Details']):
            md_content += f"- Model Details: {row['Model Details']}\n"
        if not pd.isna(row['Task']):
            md_content += f"- Task: {row['Task']}\n"
        if not pd.isna(row['Link']):
            md_content += f"- Link: {row['Link']}\n"
        if not pd.isna(row['Code/Project']):
            md_content += f"- Code/Project: {row['Code/Project']}\n"
        if not pd.isna(row['Survey Inclusion']):
            md_content += f"- Survey Inclusion: {row['Survey Inclusion']}\n"
        if not pd.isna(row['Short Summary']):
            md_content += f"- Short Summary: {row['Short Summary']}\n"
        if not pd.isna(row['Published in']):
            md_content += f"- Published in: {row['Published in']}\n"
        if not pd.isna(row['备注']):
            md_content += f"- 备注: {row['备注']}\n"

        # 将Markdown内容写入文件
        md_filename = '../_posts/' + date_formatted.split(' ')[0] +'-'+ row['Paper'] + '.md'
        with open(md_filename, 'w', encoding='utf-8') as file:
            file.write(md_content)

        print(f"{md_filename} has been created.")
      
  