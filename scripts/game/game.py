
import random
from .board import Board
from .snake import Snake
from .fruit import Fruit
from .vect2d import Vect2d

FRUIT_RATE = 1
SNAKE1_HEAD = 1
SNAKE1_BODY = 2
SNAKE2_HEAD = 3
SNAKE2_BODY = 4
SNAKE3_HEAD = 5
SNAKE3_BODY = 6

class SnakeGame:
    def __init__(self, dim, msDelay):
        self.gameRunning = False
        self.board = Board(dim)
        self.snakes = [Snake(False, 1, self.board.squares), Snake(True, 2, self.board.squares)]
        self.numSnakes = 1
        self.keysPressed = set()
        self.fruits = []
        self.msDelay = msDelay
       
    def checkGame(self, snake):
        if snake.isOutOfBoard(self.board.dimension):
            self.gameRunning = False
            snake.alive = False

        if snake.checkCollisionSnakes(self.snakes):
            self.gameRunning = False
            snake.alive = False

    def initGame(self):
        for snake in self.snakes:
            snake.incrementLenght(3)
            self.board.setElementPos(snake.position[0], SNAKE1_HEAD)
            self.board.setElementPos(snake.position[1], SNAKE1_BODY)
            self.board.setElementPos(snake.position[2], SNAKE1_BODY)

        self.fruits = [self.createFruit()]

    def moveSnakes(self):
        for snake in self.snakes:
            snake.move(self.fruits)
            self.checkGame(snake)
            self.board.setElementPos(snake.position[0], SNAKE1_HEAD)
            for i in range(1, len(snake.position)):
                self.board.setElementPos(snake.position[i], SNAKE1_BODY)

    def createFruit(self):
        x = random.randint(0, self.board.dimension - 1)
        y = random.randint(0, self.board.dimension - 1)
        return Fruit(Vect2d(x, y), 10)
