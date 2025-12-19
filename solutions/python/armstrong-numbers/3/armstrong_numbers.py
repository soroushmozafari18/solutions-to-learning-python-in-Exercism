def is_armstrong_number(number):
    return number== sum([int(letter)**len(str(number)) for letter in str(number)])