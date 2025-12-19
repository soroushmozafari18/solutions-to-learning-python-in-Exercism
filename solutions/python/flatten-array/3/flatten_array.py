def flatten(iterable):
    mylist=[]
    def flatten_2(iterable_2):
        for value in iterable_2:
            if isinstance(value,int):
                mylist.append(value)
            elif isinstance(value,list):
                flatten_2(value)
    flatten_2(iterable)
    return mylist