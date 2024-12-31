from textnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    delimited_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            delimited_nodes.append(node)
            continue
        
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")

        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        delimited_nodes.extend(split_nodes)
    return delimited_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    