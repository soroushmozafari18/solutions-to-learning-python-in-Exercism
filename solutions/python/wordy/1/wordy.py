import re
def multiple(word,num_1:int,num_2:int):
    if word==' divided by ':
        return num_1/num_2
    elif word==' multiplied by ':
        return num_1*num_2
    elif word==' plus ':
        return num_1+num_2
    elif word==' minus ':
        return num_1-num_2
    else:
        return 'somethingswrong'
def answer(question):
    #what is 5?
    matched_list=[]
    pattern=re.compile(r'(What is )(\d+)(\?)')
    matches=pattern.finditer(question) 
    for match in matches:
        matched_list.append(int(match.group(2)))
    if len(matched_list)==0:
        pass
    else:
        return matched_list[0]
    #what is 1 plus 2?
    matched_list=[]
    pattern=re.compile(r'(What is )((\-|\+)?\d+)( plus )((\-|\+)?\d+)(\?)')
    matches=pattern.finditer(question) 
    for match in matches:
        matched_list.append(int(match.group(2)))
        matched_list.append(int(match.group(5)))        
    if len(matched_list)==0:
        pass
    else:
        return matched_list[0]+matched_list[1]
    #what is 1 minus 2?
    matched_list=[]
    pattern=re.compile(r'(What is )((\-|\+)?\d+)( minus )((\-|\+)?\d+)(\?)')
    matches=pattern.finditer(question) 
    for match in matches:
        matched_list.append(int(match.group(2)))
        matched_list.append(int(match.group(5)))        
    if len(matched_list)==0:
        pass
    else:
        return matched_list[0]-matched_list[1]
    #what is 1 multiplied by 2?
    matched_list=[]
    pattern=re.compile(r'(What is )((\-|\+)?\d+)( multiplied by )((\-|\+)?\d+)(\?)')
    matches=pattern.finditer(question) 
    for match in matches:
        matched_list.append(int(match.group(2)))
        matched_list.append(int(match.group(5)))        
    if len(matched_list)==0:
        pass
    else:
        return matched_list[0]*matched_list[1]
    #what is 6 divided by 4?
    matched_list=[]
    pattern=re.compile(r'(What is )((\-|\+)?\d+)( divided by )((\-|\+)?\d+)(\?)')
    matches=pattern.finditer(question) 
    for match in matches:
        matched_list.append(int(match.group(2)))
        matched_list.append(int(match.group(5)))        
    if len(matched_list)==0:
        pass
    else:
        return matched_list[0]/matched_list[1]
    matched_list=[]
    pattern=re.compile(r'(What is )((\-|\+)?\d+)( minus | plus | multiplied by | divided by |)((\-|\+)?\d+)( minus | plus | multiplied by | divided by |)((\-|\+)?\d+)(\?)')
    matches=pattern.finditer(question) 
    for match in matches:
        matched_list.append(int(match.group(2)))
        matched_list.append(match.group(4))
        matched_list.append(int(match.group(5)))
        matched_list.append(match.group(7))
        matched_list.append(int(match.group(8)))   
    if len(matched_list)==0:
        pass
    else:
        x=multiple(matched_list[1],matched_list[0],matched_list[2])
        return multiple(matched_list[3],x,matched_list[4])
    if 'cubed'in question:
        raise ValueError("unknown operation")
    elif 'President' in question:
        raise ValueError("unknown operation")
    else:
        raise ValueError("syntax error")
    
    
    