def equilateral(sides):
    return (sides[0]==sides[1] and sides[1]==sides[2]) if((sum(sides)>=(sides[0]*2) and sum(sides)>=(sides[1]*2) and sum(sides)>=(sides[2]*2))and ((sides[0] and sides[1] and sides[2])>0)) else False


def isosceles(sides):
    return ((sides[0]==sides[1] and sides[1]!=sides[2])or(sides[0]==sides[2] and sides[1]!=sides[2])or(sides[1]==sides[2] and sides[0]!=sides[2])or(sides[0]==sides[1] and sides[1]==sides[2])) if((sum(sides)>=(sides[0]*2) and sum(sides)>=(sides[1]*2) and sum(sides)>=(sides[2]*2))and ((sides[0] and sides[1] and sides[2])>0)) else False



def scalene(sides):
    return (sides[0]!=sides[1] and sides[0]!=sides[2] and sides[1]!=sides[2]) if((sum(sides)>=(sides[0]*2) and sum(sides)>=(sides[1]*2) and sum(sides)>=(sides[2]*2))and ((sides[0] and sides[1] and sides[2])>0)) else False
