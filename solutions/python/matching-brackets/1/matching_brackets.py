def is_paired(input_string):
    for letter in input_string:
        if letter not in '[]{}()':
            input_string=input_string.replace(letter,'')
    paran_list=['[]','{}','()']
    while any(c in input_string for c in paran_list):
        for character in paran_list:
            if character in input_string:
                input_string=input_string.replace(character,'')
    return True if not input_string else False