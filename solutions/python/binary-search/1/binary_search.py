def find(search_list, value):
    pre_deleted=[]
    while search_list!=[]:
        the_middle=search_list[len(search_list)//2]
        if value==the_middle:
            return (search_list.index(the_middle)+len(pre_deleted))
        elif value>the_middle:
            pre_deleted.extend(search_list[:len(search_list)//2+1])
            del search_list[:len(search_list)//2+1]
        else:
            del search_list[len(search_list)//2:]
    if search_list==[]:
        raise ValueError("value not in array")