import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image
)
def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    res = split_nodes_link(nodes)
    return res

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    res =[]
    for node in old_nodes:
        if node.text_type!=text_type_text:
            res.append(node)
            continue
        l = node.text.split(delimiter)
        if len(l)%2==0:
            raise Exception('Invalid Markdown')
        
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


def split_nodes_link(old_nodes):
    res=[]
    pattern = r'\[.*?\]\(.*?\)'
    pattern_link = r'\[(.*?)\]\((.*?)\)'
    for node in old_nodes:
        if node.text_type != text_type_text:
            res.append(node)
            continue
        #checking if the text have links
        links = extract_markdown_links(node.text)
        if len(links)==0:
            res.append(node)
            continue
        #splitting into parts using pattern
        parts = re.split(f'({pattern})',node.text)
        #Itterating through every part
        for part in parts:
            if  part =='':
                continue
            #Finding mathces for (smt)[smt] stirng
            match = re.match(pattern_link,part)
            # 
            if match:
                text = match.group(1)
                url = match.group(2)
                n = TextNode(text,text_type_link,url)
                res.append(n)
            else:
                n = TextNode(part,text_type_text)
                res.append(n)


    return res

def split_nodes_image(old_nodes):
    res=[]
    pattern = r'\[.*?\]\(.*?\)'
    pattern_link = r'\[(.*?)\]\((.*?)\)'
    for node in old_nodes:
        if node.text_type != text_type_text:
            res.append(node)
            continue
        images = extract_markdown_images(node.text)
        if len(images)==0:
            res.append(node)
            continue
        #splitting into parts using pattern
        parts = re.split(f'({pattern})',node.text)
        #Itterating through every part
        for part in parts:
            if  part =='!' or part =='':
                continue
            #Finding mathces for (smt)[smt] stirng
            match = re.match(pattern_link,part)
            # 
            if match:
                text = match.group(1)
                url = match.group(2)
                n = TextNode(text,text_type_image,url)
                res.append(n)
            else:
                n = TextNode(part[:-1],text_type_text)
                res.append(n)


    return res



text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
print(text_to_textnodes(text))