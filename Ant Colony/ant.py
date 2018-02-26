import math

def Distance(x,y):
    return math.sqrt(abs(x.x-y.x)**2 + abs(x.y-y.y)**2)

class Ant:

    #Index of the first point in the route
    first_point = -1

    def __init__(self,f_p):
        self.first_point = f_p
