

class Vect2d:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def equals(self, pos):
        return (pos.x == self.x) and (pos.y == self.y)

    def add(self, vect):
        vecR = Vect2d(self.x + vect.x, self.y + vect.y)
        return vecR
    
    def sub(self, vect):
        vecR = Vect2d(self.x - vect.x, self.y - vect.y)
        return vecR
    
    def rotateL(self):
        newDir = Vect2d(self.x, self.y)
        if(newDir.x == 1):
            newDir.x = 0
            newDir.y = -1
        elif(newDir.x == -1):
            newDir.x = 0
            newDir.y = 1
        elif(newDir.y == 1):
            newDir.y = 0
            newDir.x = 1
        elif(newDir.y == -1):
            newDir.y = 0
            newDir.x = -1

        return newDir


    def rotateR(self):
        newDir = Vect2d(self.x, self.y)
        if(newDir.x == 1):
            newDir.x = 0
            newDir.y = 1
        elif(newDir.x == -1):
            newDir.x = 0
            newDir.y = -1
        elif(newDir.y == 1):
            newDir.y = 0
            newDir.x = -1
        elif(newDir.y == -1):
            newDir.y = 0
            newDir.x = 1

        return newDir
