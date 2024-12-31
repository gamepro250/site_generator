import unittest

from textnode import TextNode, TextType
from htmlnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertTrue(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "Boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "Boot.dev")
        self.assertTrue(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_enum_exception(self):
        with self.assertRaises(ValueError) as context:
            node = TextNode("This is a text node", "Not Test Type")
        self.assertEqual(str(context.exception), "Invalid text_type: Not Test Type")

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )    

    def test_text_to_html(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        modified_node = node.text_node_to_html_node()
        self.assertEqual("LeafNode(None, This is a text node, None)", repr(modified_node)) 
        self.assertEqual("This is a text node", modified_node.value)   

    def test_bold_to_html(self):
        node = TextNode("This is a bold node", TextType.BOLD, "https://www.boot.dev")
        modified_node = node.text_node_to_html_node()
        self.assertEqual("LeafNode(b, This is a bold node, None)", repr(modified_node)) 
        self.assertEqual("b", modified_node.tag)     

    def test_image_to_html(self):
        node = TextNode("Alt Text", TextType.IMAGE, "https://www.boot.dev")
        modified_node = node.text_node_to_html_node()
        self.assertEqual("LeafNode(img, , {'src': 'https://www.boot.dev', 'alt': 'Alt Text'})", repr(modified_node)) 
        self.assertEqual("img", modified_node.tag)  

    def test_image_no_url(self):
        with self.assertRaises(ValueError) as context:
            node = TextNode("Alt Text", TextType.IMAGE)
            modified_node = node.text_node_to_html_node()
        self.assertEqual(str(context.exception), "url required for type TextType.IMAGE")

    def test_link_no_url(self):
        with self.assertRaises(ValueError) as context:
            node = TextNode("Alt Text", TextType.LINK)
            modified_node = node.text_node_to_html_node()
        self.assertEqual(str(context.exception), "url required for type TextType.LINK")

if __name__ == "__main__":
    unittest.main()