import unittest

from htmlnode import *


class TestTextNode(unittest.TestCase):
    def test_print(self):
        tag = "h1"
        value = "this is header text"
        children = None
        props = {"href": "https://www.google.com", "target": "_blank"}
        props_as_str = ' href="https://www.google.com" target="_blank"'

        test_html_node = HTMLNode(tag, value, children, props)
        self.assertTrue(repr(test_html_node), 
                f'Tag: {tag}\nValue: {value}\nChildren: {children}\nProps: {props_as_str}') 

    def test_props_to_html(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        props_as_str = ' href="https://www.google.com" target="_blank"'

        test_html_node = HTMLNode(None, None, None, props)

        self.assertEqual(test_html_node.props_to_html(), props_as_str)

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )
        
    def test_leaf(self):
        tag = "h1"
        value = "this is header text"
        props = {"href": "https://www.google.com"}        
        test_leaf_node = LeafNode(tag, value, props= props)
        HTML_tag = '<h1 href="https://www.google.com">this is header text</h1>'

        self.assertEqual(test_leaf_node.to_html(), HTML_tag)

    def test_no_value_exception(self):
        with self.assertRaises(ValueError) as context:
            node = LeafNode("h1", None)
            node.to_html()
        self.assertEqual(str(context.exception), "Invalid HTML: no value")

    def test_parent_one_leaf(self):
        tag = "b"
        value = "bold text"

        tag_parent = "p"
        props_parent = {"href": "https://www.parent.com"}

        test_leaf_node = LeafNode(tag, value)
        test_parent_node = ParentNode(tag_parent, [test_leaf_node], props_parent)

        self.assertEqual(test_parent_node.to_html(), '<p href="https://www.parent.com"><b>bold text</b></p>')
        
    def test_parent_many_leaf(self):
        tag = "b"
        value = "bold text"
        tag2 = "i"
        value2 = "italic text"

        tag_parent = "p"
        props_parent = {"href": "https://www.parent.com"}

        test_leaf_node = LeafNode(tag, value)
        test_leaf_node2 = LeafNode(tag2, value2)
        test_parent_node = ParentNode(tag_parent, [test_leaf_node,test_leaf_node2], props_parent)

        self.assertEqual(test_parent_node.to_html(), '<p href="https://www.parent.com"><b>bold text</b><i>italic text</i></p>')

        
    def test_parent_with_parent(self):
        tag = "b"
        value = "bold text"
        tag2 = "i"
        value2 = "italic text"

        tag_parent = "p"
        props_parent = {"href": "https://www.parent.com"}
        tag_parent2 = "h1"
        props_parent2 = {"href": "https://www.otherparent.com"}

        test_leaf_node = LeafNode(tag, value)
        test_leaf_node2 = LeafNode(tag2, value2)
        test_parent_node = ParentNode(tag_parent, [test_leaf_node,test_leaf_node2], props_parent)
        test_parent_node2 = ParentNode(tag_parent2, [test_parent_node], props_parent2)

        self.assertEqual(test_parent_node2.to_html(), '<h1 href="https://www.otherparent.com"><p href="https://www.parent.com"><b>bold text</b><i>italic text</i></p></h1>')

        
    def test_parent_no_tag(self):
        with self.assertRaises(ValueError) as context:
            test_parent_node = ParentNode(None, [LeafNode("b", "leaf")], {"href": "https://www.otherparent.com"})
            test_parent_node.to_html()
        self.assertEqual(str(context.exception), "Invalid HTML: no tag")

        
    def test_parent_no_children(self):
        with self.assertRaises(ValueError) as context:
            test_parent_node = ParentNode("p", [], {"href": "https://www.otherparent.com"})
            test_parent_node.to_html()
        self.assertEqual(str(context.exception), "Invalid HTML: no children")

        
    def test_parent_invalid_children(self):
        with self.assertRaises(ValueError) as context:
            test_parent_node = ParentNode("p", ["test string"], {"href": "https://www.otherparent.com"})
            test_parent_node.to_html()
        self.assertEqual(str(context.exception), "Invalid HTML: child object is not valid")

        

if __name__ == "__main__":
    unittest.main()