import os
import re
from collections import defaultdict

def extract_md_data(md_content):
    data = {}
    # Extract metadata section
    pattern = re.compile(r'^---\n(.*?)\n---\n', re.DOTALL)
    match = pattern.match(md_content)
    if match:
        metadata = match.group(1)
        for line in metadata.split('\n'):
            if ': ' in line:
                key, value = line.split(': ', 1)
                data[key.strip()] = value.strip()
    
    # Extract specific fields from the content
    lines = md_content.split('\n')
    for line in lines:
        if line.startswith('title'):
            data['title'] = line.split(': ')[1].strip()
        elif line.startswith('- Published in:'):
            data['Published in'] = line.split(': ')[1].strip()
        elif line.startswith('- tags:'):
            data['tags'] = line.split(': ')[1].strip().replace('[','').replace(']','').replace(' ','')
        elif line.startswith('categories:'):
            data['categories'] = line.split(': ')[1].strip().replace('[','').replace(']','').replace(' ','')
        elif line.startswith('- Link:'):
            data['paper_Link'] = line.split(': ')[1].strip()
        elif line.startswith('- 代码源链接'):
            data['dataset_Link'] = line.split(': ')[1].strip()
      
    return data

def sanitize_tag(tag):
    return tag.replace('[', '').replace(']', '').replace(' ', '')

def generate_readme(md_files_data):
    readme_content = "# README\n\n"

    tags_dict = defaultdict(lambda: defaultdict(list))
    
    for data in md_files_data:
        title = data.get('title', 'N/A')
        published_in = data.get('Published in', 'N/A')
        categories = data.get('categories', 'N/A')
        paper_Link = data.get('paper_Link', 'N/A')
        dataset_Link = data.get('dataset_Link', 'N/A')
        tags = [sanitize_tag(tag) for tag in data.get('tags', '').split(',')]
        first_tag = tags[0] if tags else 'Other'
        second_tag = tags[1] if len(tags) > 1 else 'General'
        detailed_link = f"https://irip-buaa.github.io/posts/{title.replace(' ', '-')}"

        tags_dict[first_tag][second_tag].append({
            'title': title,
            'published_in': published_in,
            'categories': categories,
            'link': detailed_link,
            'paper_Link': paper_Link,
            'dataset_Link': dataset_Link
        })

    for first_tag, second_tags in tags_dict.items():
        readme_content += f"# {first_tag}\n\n"
        for second_tag, papers in second_tags.items():
            readme_content += f"## {second_tag}\n\n"
            if first_tag.lower() == 'dataset':
                readme_content += "| Dataset Name | Categories | Detailed Info |\n"
                readme_content += "|------------|------------|---------------|\n"
                for paper in papers:
                    readme_content += f"| [{paper['title']}]({paper['dataset_Link']}) | {paper['categories']} | [Link]({paper['link']}) |\n"
            else:
                readme_content += "| Paper Name | Published in | Detailed Info |\n"
                readme_content += "|------------|--------------|---------------|\n"
                for paper in papers:
                    readme_content += f"| [{paper['title']}]({paper['paper_Link']}) | {paper['published_in']} | [Link]({paper['link']}) |\n"
            readme_content += "\n"

    return readme_content

def main():
    md_folder_path = 'D:\资料\研一\项目\遥感大模型综述\github\IRIP-BUAA.github.io\_posts'  # Replace with your actual folder path
    md_files = [f for f in os.listdir(md_folder_path) if f.endswith('.md')]

    md_files_data = []
    for md_file in md_files:
        with open(os.path.join(md_folder_path, md_file), 'r', encoding='utf-8') as file:
            md_content = file.read()
            md_data = extract_md_data(md_content)
            md_files_data.append(md_data)

    readme_content = generate_readme(md_files_data)

    with open('README.md', 'w', encoding='utf-8') as readme_file:
        readme_file.write(readme_content)

if __name__ == '__main__':
    main()
