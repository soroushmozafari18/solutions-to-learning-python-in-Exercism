def is_armstrong_number(number):
    str_number=str(number)
    return number== sum([int(letter)**len(str_number) for letter in str_number])