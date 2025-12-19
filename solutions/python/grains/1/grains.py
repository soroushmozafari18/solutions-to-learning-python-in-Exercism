
def square(number):
    if number>64 or number<1:
        raise ValueError("square must be between 1 and 64")
    else:
        return 2**(number-1)


def total():
    sum=0
    for i in range (0,64):
        sum+=2**i
    return sum
