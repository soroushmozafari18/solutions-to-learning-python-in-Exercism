def is_paired(input_string):
    brackets=[]
    opened='[{('
    closed=']})'
    for letter in input_string:
        if letter in opened:
            brackets.append(letter)
        elif letter in closed:
            if not brackets:
                return False
            elif brackets.pop()!= opened[closed.index(letter)]:
                return False
    return True if not brackets else False