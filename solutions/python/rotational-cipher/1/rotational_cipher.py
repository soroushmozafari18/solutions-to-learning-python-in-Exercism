def rotate(text, key):
    lowercase='abcdefghijklmnopqrstuvwxyz'
    uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    maindict_upper=dict()
    maindict_lower=dict()
    for i in range(0,26):
        maindict_lower[lowercase[i]]=i
    for i in range(0,26):
        maindict_upper[uppercase[i]]=i
    newdict_upper={}
    newdict_lower={}
    for item in list(maindict_upper.items()):
        newdict_upper[(item[1]+26-key)%26]=item[0]
    for item in list(maindict_lower.items()):
        newdict_lower[(item[1]+26-key)%26]=item[0]
    letters_list=[]
    for letter in text:
        if letter in list(maindict_upper.keys()):
            letters_list.append(newdict_upper[maindict_upper[letter]])
        elif letter in list(maindict_lower.keys()):
            letters_list.append(newdict_lower[maindict_lower[letter]])
        else:
            letters_list.append(letter)
    return(''.join(letters_list))

