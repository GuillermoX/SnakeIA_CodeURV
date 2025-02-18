
import math
from .vect2d import Vect2d

class Snake:

    def __init__(self, ia, id):
        self.position = [Vect2d(0,0)]       #Position of each part of the body (first is head)
        self.dir = Vect2d(1,0)              #Direction of the head
        self.lenght = 0
        self.vel = 1
        self.points = 0
        self.alive = True
        self.ia = ia                        #Specify if the snake is going to be controlled by IA or human
        self.id = id 
    
    def incrementLenght(self, increment: int):
        lenght += increment
    
    def move(self, fruits):
        newHead = self.position[0].add(self.dir)
        self.position.insert(0, newHead)

        if(not(self.headOnFruit(self.position[0], fruits))):
            self.position.pop()


    def headOnFruit(self, posHead: Vect2d, fruits):
        for fruit in fruits:
            if(posHead.equals(fruit.pos)): 
                self.points += fruit.points
                fruits.remove(fruit)
                return True

        return False

    def choseDirection(self, keysPressed, fruits, dim, snakes):
        #TODO: If the snake is controlled by AI let the AI decide
        
        if(self.ia): 
            """
            if (len(fruits) > 0):
                subVect = fruits[0].pos.sub(self.position[0])
                if subVect.x > 0:
                    self.dir.x = 1
                elif subVect.x < 0:
                    self.dir.x = -1
                else:
                    self.dir.x = 0
                
                if subVect.y > 0 :
                    self.dir.y = 1
                elif subVect.y < 0:
                    self.dir.y = -1
                else:
                    self.dir.y = 0
            else:
                firstCheck = random.choice([0,1])

                if(firstCheck == 0):

                    if self.position[0].x == 0 or self.position[0].x == dim-1: 
                        self.dir.x = 0
                        if(self.position[0].y == dim-1):
                            self.dir.y = -1
                        elif(self.position[0].y == 0):
                            self.dir.y = 1
                        else: 
                            if self.dir.y == 0:
                                self.dir.y = random.choice([-1,1])

                    if self.position[0].y == 0 or self.position[0].y == dim-1:  
                        self.dir.y = 0
                        if(self.position[0].x == dim-1):
                            self.dir.x = -1
                        elif(self.position[0].x == 0):
                            self.dir.x = 1
                        else: 
                            if self.dir.x == 0:
                                self.dir.x = random.choice([-1,1])
                else:
                    if self.position[0].y == 0 or self.position[0].y == dim-1:  
                        self.dir.y = 0
                        if(self.position[0].x == dim-1):
                            self.dir.x = -1
                        elif(self.position[0].x == 0):
                            self.dir.x = 1
                        else: 
                            if self.dir.x == 0:
                                self.dir.x = random.choice([-1,1])
 
                    if self.position[0].x == 0 or self.position[0].x == dim-1: 
                        self.dir.x = 0
                        if(self.position[0].y == dim-1):
                            self.dir.y = -1
                        elif(self.position[0].y == 0):
                            self.dir.y = 1
                        else: 
                            if self.dir.y == 0:
                                self.dir.y = random.choice([-1,1])
           """
            decision = self.moveDecision(fruits, dim, snakes)
            if(decision == 1): self.dir = self.dir.rotateL()
            elif(decision == 2): self.dir = self.dir.rotateR()
            elif(decision == 3): self.dir = Vect2d(0,0)
        else:
            if ord('d') in keysPressed and self.dir.x == 0:
                self.dir = Vect2d(1,0)
            if ord('a') in keysPressed and self.dir.x == 0:
                self.dir = Vect2d(-1,0)
            if ord('w') in keysPressed and self.dir.y == 0: 
                self.dir = Vect2d(0,-1)
            if ord('s') in keysPressed and self.dir.y == 0: 
                self.dir = Vect2d(0,1)


    def moveDecision(self, fruits, dim, snakes):
        #return random.choice([1,2])

        optionProb = [0,0,0]

        if(len(fruits) > 0):
            actualPos = self.position[0]

            closestFruit = self.closestFruit(fruits)

            #Straight
            self.position[0] = self.position[0].add(self.dir)
            if(self.checkCollisionSnakes(snakes) or self.isOutOfBoard(dim)):
                optionProb[0] = 10000
            else:
                diffPos = closestFruit.pos.sub(self.position[0])
                optionProb[0] = math.sqrt(diffPos.x*diffPos.x + diffPos.y*diffPos.y)

            #Left
            self.position[0] = actualPos
            self.position[0] = self.position[0].add(self.dir.rotateL())
            if(self.checkCollisionSnakes(snakes) or self.isOutOfBoard(dim)):
                optionProb[1] = 10000
            else:
                diffPos = closestFruit.pos.sub(self.position[0])
                optionProb[1] = math.sqrt(diffPos.x*diffPos.x + diffPos.y*diffPos.y)

            #Right
            self.position[0] = actualPos
            self.position[0] = self.position[0].add(self.dir.rotateR()) 
            if(self.checkCollisionSnakes(snakes) or self.isOutOfBoard(dim)):
                optionProb[2] = 10000
            else:
                diffPos = closestFruit.pos.sub(self.position[0])
                optionProb[2] = math.sqrt(diffPos.x*diffPos.x + diffPos.y*diffPos.y)

            self.position[0] = actualPos

            if(optionProb[0] <= optionProb[1] and optionProb[0] <= optionProb[2]): return 0
            elif(optionProb[1] <= optionProb[0] and optionProb[1] <= optionProb[2]): return 1
            elif(optionProb[2] <= optionProb[0] and optionProb[2] <= optionProb[1]): return 2

        else: return 1



    def onPosition(self, pos: Vect2d):
        for bodyPart in self.position:
            if(bodyPart.equals(pos)): return True 

        return False

    def isOutOfBoard(self, dim): 
        if (self.position[0].x < 0) or (self.position[0].x >= dim) or\
            (self.position[0].y < 0) or (self.position[0].y >= dim):
            return True
        else:
            return False

    def checkCollisionSnakes(self, snakes):
        for snake in snakes:
            pos = 0
            for position in snake.position:
                if (self.position[0].equals(position)) and (pos>0 or (pos == 0 and self.id != snake.id)): return True
                pos += 1
        return False

    def closestFruit(self, fruits):

        diffVect = fruits[0].pos.sub(self.position[0])
        distMin = diffVect.x*diffVect.x + diffVect.y*diffVect.y
        fruitMin = fruits[0]
        for fruit in fruits:
            diffVect = fruit.pos.sub(self.position[0])
            dist = diffVect.x*diffVect.x + diffVect.y*diffVect.y
            if(dist < distMin): 
                fruitMin = fruit
                distMin = dist

        return fruitMin