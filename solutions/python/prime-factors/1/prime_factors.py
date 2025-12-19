def factors(value):
    return myfactors(value,[])
def myfactors(value,my_list):
    
    for i in range(2,value+1):
        if not value%i:
            my_list.append(i)
            return myfactors(int(value/i),my_list)
    return my_list
