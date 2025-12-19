"""Functions to keep track and alter inventory."""


def create_inventory(items):
    mydict={}
    for word in items:
        mydict[word]=mydict.get(word,0)+1   
    return mydict
  

def add_items(inventory, items):
    for key,value in list(inventory.items()):
        addable_list=[key]*value
        print(addable_list)
        items.extend(addable_list)
    print(items)
    return create_inventory(items)
            
    
    

def decrement_items(inventory, items):
    for word in items:
        if inventory[word]==0:
             continue   
        else:
             inventory[word]=inventory.get(word)-1
    return inventory

def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    else:
        pass
    return inventory


def list_inventory(inventory):
    mylist=list(inventory.items())
    for item,number in mylist:
        if number==0:
            mylist.remove((item,number))
    return mylist