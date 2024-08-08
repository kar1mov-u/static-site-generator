class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None) -> None:
        self.tag  = tag
        self.value = value
        self.children  =children
        self.props = props
    def to_html(self):
        raise NotImplemented
    
    def props_to_html(self):
        if not self.props:
            return '' 
        res=''
        for k in self.props.keys():
            res+=f' {k}="{self.props[k]}"'
        return res
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})"
    
    def __eq__(self,target) -> bool:
        return (
            self.tag == target.tag and
            self.value == target.value and
            self.children == target.children and 
            self.props == target.props
        )


class LeafNode(HTMLNode):
    def __init__(self, tag,   value,props=None) -> None:
        super().__init__(tag, value,None,props)

    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return self.value
        
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError('Tag is not included')
        if not self.children:
            raise ValueError ('CHILDREN list is empty')
        children_html=''
        for child in self.children:
            children_html+=child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
    





    


