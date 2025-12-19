import re
def flatten(iterable):
    mylist=[]
    iterable=str(iterable)
    pattern=re.compile(r'[\+\-]?\d+')
    matches=pattern.finditer(iterable)
    for match in matches:
        mylist.append(int(match.group(0)))
    return mylist