def score(x, y):
    if x**2+y**2<=100:
        if x**2+y**2<=25:
            if x**2+y**2<=1:
                return 10
            else:
                return 5
        else:   
            return 1
    else:
        return 0