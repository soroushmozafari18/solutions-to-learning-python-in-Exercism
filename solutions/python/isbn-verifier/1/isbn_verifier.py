def is_valid(isbn):
    isbn=isbn.replace('-','')
    sum_isbn=0
    if len(isbn)!=10:
        return False
    else:
        pass
    for i in range(0,9):
        if isbn[i] not in '1234567890':
            return False
        else:
            pass
        sum_isbn+= int(isbn[i])*(10-i)
    if isbn[9]=='X':
        sum_isbn+= 10
    elif isbn[9] not in '1234567890':
        return False
    else:
        sum_isbn+= int(isbn[9])
    return not sum_isbn%11
