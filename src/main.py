from textnode import *
from htmlnode import *
from inline_markdown import *

def main():

    testNode = TextNode("This is a text node", TextType.BOLD, "http://testurl.com")
    #print(testNode)

    tag = "h1"
    value = "this is header text"
    props = {"href": "https://www.google.com", "target": "_blank"}

    test_html_node = HTMLNode(tag, value, children=None, props= props)
    #print(test_html_node)

    test_leaf_node = LeafNode(tag, value, props= props)
    #print(test_leaf_node.to_html())

    tag_parent = "p"
    children_parent = [test_leaf_node, test_leaf_node]
    props_parent = {"href": "https://www.parent.com"}

    test_parent_node = ParentNode(tag_parent, children_parent, props_parent)
    #print(test_parent_node.to_html())

    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))

    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text))
    
main()