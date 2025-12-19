def append(list1, list2):
    return list1+list2


def concat(lists):
    final_list=[]
    for item in lists:
        if isinstance(item,list) and (isinstance(i,int) for i in item):
            for i in item:
                final_list.append(i)
        elif isinstance(item,list) and len(item)==1:
            for i in item:
                final_list.append(i)
    return final_list



def filter(function, list):
    new_list=[]
    for item in list:
        if function(item):
            new_list.append(item)
    return new_list


def length(list):
    count=0
    for i in list:
        count+=1
    return count

def map(function, list):
    for i in range(0,len(list)):
        list[i]=function(list[i])
    return list
        


def foldl(function, list, initial):
    for item in list:
        initial=function(initial,item)
    return initial
        


def foldr(function, list, initial):
    for i in range(0,len(list)):
        initial=function(initial,list[len(list)-(i+1)])
    return initial


def reverse(my_list):
    return list(my_list[i] for i in range(len(my_list)-1,-1,-1))
        
