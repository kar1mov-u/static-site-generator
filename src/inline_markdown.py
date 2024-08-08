import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    res =[]
    for node in old_nodes:
        if node.text_type!=text_type_text:
            res.append(node)
            continue
        l = node.text.split(delimiter)
        if len(l)%2==0:
            raise Exception('Invalid Markdown')
        print(l)
        for i in range(len(l)):
            if l[i]=="":
                continue
            if i%2==0:
                r = TextNode(l[i],text_type_text)
                res.append(r)
            else:
                r = TextNode(l[i],text_type)
                res.append(r)

    return res



def extract_markdown_images(text):
    images = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    return images

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)",text)
    return links
