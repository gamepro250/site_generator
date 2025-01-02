import os
import shutil
from markdown_blocks import markdown_to_html_node, extract_title
from htmlnode import *
from pathlib import Path

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    f = open(from_path)
    markdown = f.read()
    f.close()

    f = open(template_path)
    template = f.read()
    f.close()

    markdown_to_nodes = markdown_to_html_node(markdown)
    html_from_nodes = markdown_to_nodes.to_html()

    title = extract_title(markdown)

    template_titled = template.replace("{{ Title }}", title)
    content = template_titled.replace("{{ Content }}", html_from_nodes)

    dirname = os.path.dirname(dest_path)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(content)    

def generate_pages_recursive(path_dir_content, template_path, dest_dir_path):
    dir_list = os.listdir(path_dir_content)

    for content in dir_list:
        from_path = os.path.join(path_dir_content, content)
        dest_path = os.path.join(dest_dir_path, content)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)