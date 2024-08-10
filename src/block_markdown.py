def markdown_to_blocks(markdown):
    res = []
    lines = markdown.split('\n\n')
    for line in lines:
        if line =="":
            continue
        line=line.strip()
        res.append(line)
    return res
    
def block_to_block_type(block):
    if block.startswith('#'):
        return 'heading'
    
    lines = block.split('\n')
    if len(lines) >= 2 and lines[0][:3] == '```' and lines[-1][-3:] == '```':
        return 'code'
    if lines:
        quote_check = True
        unorder_list = True
        ordered_list = True
        


    for line in lines:
        if line[0] != '>':
            quote_check = False
    if quote_check:
        return 'quote'
    
    for line in lines:
        if line[:2]!= '* ' and line[:2]!='- ':
            unorder_list = False
    if unorder_list:
        return 'unordered_list'
    
    prev=1
    for line in lines:
        if line[:3]!=f'{prev}. ':
            ordered_list=False
        prev+=1
    if ordered_list:
        return 'ordered_list'
    
    return 'paragraph'
    
print(block_to_block_type('* This is a heading'))