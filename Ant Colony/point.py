class Point:
    x = 0
    y = 0
    pheromone_number = 0

    def __init__(self,x_p,y_p):
        self.x = x_p
        self.y = y_p

    def AddPheromone(self):
        self.pheromone_number+=1

    def RemovePheromone(self):
        if self.pheromone_number>0:
            self.pheromone_number-=1

    def Iteration(self,add):
        if add:
            self.AddPheromone()
        else:
            self.RemovePheromone()
