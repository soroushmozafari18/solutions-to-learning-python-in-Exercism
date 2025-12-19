"""Solution to Ellen's Alien Game exercise."""


class Alien:
    health=3
    total_aliens_created=0
    def __init__(self,number_x,number_y):
        self.x_coordinate=number_x
        self.y_coordinate=number_y
        Alien.total_aliens_created+=1
    def hit(self):
        self.health+=(-1)
    def is_alive(self):
        return self.health>0
    def teleport(self,coordinate_x,coordinate_y):
        self.x_coordinate=coordinate_x
        self.y_coordinate=coordinate_y
    def collision_detection(self,coordinates):
        pass

def new_aliens_collection(alienslist):
    newlist=[]
    for eachtuple in alienslist:
        new_alien=Alien(eachtuple[0],eachtuple[1])
        newlist.append(new_alien)
    return newlist