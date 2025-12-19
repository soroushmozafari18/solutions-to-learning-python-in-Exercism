def is_isogram(mystring):
    import string
    mystring=mystring.lower()
    for letter in mystring:
        if letter not in string.ascii_lowercase:
            mystring=mystring.replace(letter,'')
    for letter in mystring:
        string2=mystring.replace(letter,'')
        if len(mystring)-len(string2)>1:
            return False
        else:
            pass
    return True
