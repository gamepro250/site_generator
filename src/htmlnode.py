class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        html_string = ""
        for key, value in self.props.items():
           html_string += f' {key}="{value}"'
        return html_string
    
    def __repr__(self):
        return(f"Tag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps: {self.props_to_html()}")
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None or self.children == []:
            raise ValueError("Invalid HTML: no children")
        nested_html = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            if isinstance(child, HTMLNode):
                child_html = child.to_html()
                nested_html = nested_html + child_html
            else:
                raise ValueError("Invalid HTML: child object is not valid")
        nested_html += f"</{self.tag}>"
        return nested_html

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"