from numpy import array, delete
from random import randint
from Game_Objects.global_vars import MAX_X, MAX_Y, OX, OY, AMOUNT
from Game_Objects.obstacle_class import Obstacle


class ObstacleArray():
    def __init__(self, window):
        self.obstacles = array([Obstacle(window)
                                for _ in range(len(OX))])  # list of Obstacle objects
        self.active = 0
        OX2 = OX.copy()
        OY2 = OY.copy()
        for obstacle in self.obstacles:
            rand = randint(0, len(OX2) - 1)  # choosing random index
            obstacle.coordinate = OX2[rand], OY2[rand]
            OX2 = delete(OX2, rand)  # removing used coordinates from lists
            OY2 = delete(OY2, rand)  # doesn't allow to choose them again

    def render(self):
        for obstacle in self.obstacles:
            obstacle.render()

    def update(self):
        if self.active < AMOUNT:
            self.obstacles[self.active].exist = True  # now spike exists
            self.active += 1
