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

def split_nodes_image(old_nodes):
    delimited_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            delimited_nodes.append(node)
            continue
        
        original_text = node.text
        images = extract_markdown_images(original_text)
        if not images:
            delimited_nodes.append(node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                delimited_nodes.append(TextNode(sections[0], TextType.TEXT))
            delimited_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            original_text = sections[1]
        if original_text != "":
            delimited_nodes.append(TextNode(original_text, TextType.TEXT))
    return delimited_nodes

def split_nodes_link(old_nodes):
    delimited_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            delimited_nodes.append(node)
            continue
        
        original_text = node.text
        links = extract_markdown_links(original_text)
        if not links:
            delimited_nodes.append(node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                delimited_nodes.append(TextNode(sections[0], TextType.TEXT))
            delimited_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            delimited_nodes.append(TextNode(original_text, TextType.TEXT))
    return delimited_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_link(nodes)
    return  split_nodes_image(nodes)


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches
