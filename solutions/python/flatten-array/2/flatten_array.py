def flatten(iterable):
    mylist=[]
    for value in iterable:
        if isinstance(value,list):
            for value_1 in value:
                if isinstance(value_1,list):
                    for value_2 in value_1:
                        if isinstance(value_2,list):
                            for value_3 in value_2:
                                if isinstance(value_3,list):
                                    for value_4 in value_3:
                                        if isinstance(value_4,int):
                                            mylist.append(value_4)
                                elif isinstance(value_3,int):        
                                    mylist.append(value_3)
                        elif isinstance(value_2,int):
                            mylist.append(value_2)
                elif isinstance(value_1,int):            
                    mylist.append(value_1)
        elif isinstance(value,int):
            mylist.append(value)
    for i in mylist:
        if isinstance(i,int):
            pass
        else:
            mylist.remove(i)
    return mylist