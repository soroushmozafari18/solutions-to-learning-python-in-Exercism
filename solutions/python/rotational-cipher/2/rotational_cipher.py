def rotate(text, key):
    lowercase='abcdefghijklmnopqrstuvwxyz'
    uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    the_only_dict={}
    for letter in lowercase:
        the_only_dict[letter]=lowercase[(lowercase.find(letter)+key)%26]
    for letter in uppercase:
        the_only_dict[letter]=uppercase[(uppercase.find(letter)+key)%26]
    letters_list=[]
    for letter in text:
        if letter in  lowercase:
            letters_list.append(the_only_dict[letter])
        elif letter in uppercase:
            letters_list.append(the_only_dict[letter])
        else:
            letters_list.append(letter)
    return(''.join(letters_list))


