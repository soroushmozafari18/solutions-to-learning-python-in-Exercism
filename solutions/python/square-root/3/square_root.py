def square_root(number):
    return sum(i if i**2==number else 0 for i in range(0,number+1))