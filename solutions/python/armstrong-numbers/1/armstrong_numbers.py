def is_armstrong_number(number):
    str_number=str(number)
    sum=0
    for letter in str_number:
        sum+=int(letter)**len(str_number)
    if number==sum:
        return True
    else:
        return False
