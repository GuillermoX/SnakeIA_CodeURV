
from .vect2d import Vect2d

EMPTY = 0

class Board:
    def __init__(self, dimension: int):
        self.dimension = dimension
        self.boxes = [[EMPTY]*self.dimension for _ in range(self.dimension)]

    def setElementPos(self, element: int, position: Vect2d):
        self.boxes[position.y][position.x] = element
