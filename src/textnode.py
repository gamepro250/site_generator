from enum import Enum
from htmlnode import *

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        if isinstance(text_type, TextType):
            self.text_type = text_type
        else:
            # Handle the error or set a default
            raise ValueError(f"Invalid text_type: {text_type}")
        self.url = url

    def __eq__(self, otherNode):
        return(self.text == otherNode.text 
           and self.text_type == otherNode.text_type 
           and self.url == otherNode.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    def text_node_to_html_node(self):
        link_dict = {"href": f"{self.url}"}
        image_dict = {"src": f"{self.url}", "alt": f"{self.text}"}
        match self.text_type:
            case TextType.TEXT:
                return LeafNode(None, self.text, None)
            case TextType.BOLD:
                return LeafNode("b", self.text, None)
            case TextType.ITALIC:
                return LeafNode("i", self.text, None)                
            case TextType.CODE:
                return LeafNode("code", self.text, None)
            case TextType.LINK:
                if self.url is None:
                    raise ValueError(f"url required for type {self.text_type}")
                return LeafNode("a", self.text, link_dict)
            case TextType.IMAGE:
                if self.url is None:
                    raise ValueError(f"url required for type {self.text_type}")
                return LeafNode("img", "", image_dict)