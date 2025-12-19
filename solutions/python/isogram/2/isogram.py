def is_isogram(mystring):
    import string
    mystring=mystring.lower()
    for letter in mystring:
        if letter not in string.ascii_lowercase:
            mystring=mystring.replace(letter,'')
    return len(mystring)==len(set(mystring))
