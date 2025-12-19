def score(x, y):
    if 25<x**2+y**2<=100:
        return 1
    elif 1<x**2+y**2<=25:
        return 5
    elif x**2+y**2<=1:
        return 10
    else:
        return 0