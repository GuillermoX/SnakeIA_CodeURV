
import random
import curses

from .board import Board
from .snake import Snake
from .fruit import Fruit
from .vect2d import Vect2d

from config import *


class SnakeGame:

    def __init__(self, dim, msDelay, stdscr):
        self.stdscr = stdscr
        self.gameRunning = False
        self.board = Board(dim)
        self.snakes = [Snake(False, 1), Snake(True, 2)]
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

            #TODO: Check if the snake head has crashed his own body

    def initSnakes(self):
        for snake in self.snakes:
            snake.position[0].x = random.randint(1, self.board.dimension-2)
            snake.position[0].y = random.randint(1, self.board.dimension-2)

    def getKeys(self):
        keys = self.stdscr.getch()
        if keys != -1 and not(keys in self.keysPressed):
            self.keysPressed.add(keys)
        else:
            self.keysPressed.clear()

    def generateFruit(self, snakes):
        illegalPos = True
        while(illegalPos):
            randomPos = Vect2d(random.randint(0, self.board.dimension-1), random.randint(0, self.board.dimension-1))
            illegalPos = False
            for snake in snakes:
                if(snake.onPosition(randomPos)):
                    illegalPos = True
                    break

    
        newFruit = Fruit(randomPos, 10)
        self.fruits.append(newFruit)

    def runGame(self):
        self.gameRunning = True
        self.initSnakes()
        timeCount = 0

        while self.gameRunning:
            self.getKeys() 

            if(timeCount >= FRUIT_RATE*(1000/self.msDelay)):
                timeCount = 0
                self.generateFruit(self.snakes)

            for snake in self.snakes:
                snake.choseDirection(self.keysPressed, self.fruits, self.board.dimension, self.snakes)
                snake.move(self.fruits)
                self.checkGame(snake)
                if not(self.gameRunning):
                    return
                self.updateBoard()
                self.printGameState()

            timeCount += 1

        


    def updateBoard(self):
        row_i = 0
        for row in self.board.boxes:
            col_i = 0
            for box in row:
                position = Vect2d(col_i, row_i)
                element = self.getElementPos(position)
                self.board.setElementPos(element, position)
                col_i += 1

            row_i += 1

    def getElementPos(self, pos: Vect2d):
        for fruit in self.fruits:
            if(fruit.pos.equals(pos)): return FRUIT

        snake_i = 0
        for snake in self.snakes:
            if snake.position[0].equals(pos): return snake_i*2 + 1
            snake_i += 1

        snake_i = 0
        for snake in self.snakes:
            if snake.onPosition(pos): return (snake_i+1)*2
            snake_i += 1

        return 0

    


    def printGameState(self):
        self.stdscr.clear()
        row_i = 0
        for row in self.board.boxes:
            col_i = 0
            for col in row:
                element = '0'
                if col == EMPTY:
                    element = '·'
                    self.stdscr.addch(row_i, col_i, element)
                elif col == SNAKE1_HEAD:
                    element = '@'
                    self.stdscr.addch(row_i, col_i, element, curses.color_pair(1))
                elif col == SNAKE1_BODY:
                    element = '#'
                    self.stdscr.addch(row_i, col_i, element, curses.color_pair(1))
                elif col == SNAKE2_HEAD:
                    element = '&'
                    self.stdscr.addch(row_i, col_i, element, curses.color_pair(2))
                elif col == SNAKE2_BODY:
                    element = '$' 
                    self.stdscr.addch(row_i, col_i, element, curses.color_pair(2))
                elif col == SNAKE3_HEAD:
                    element = '%'
                    self.stdscr.addch(row_i, col_i, element, curses.color_pair(3))
                elif col == SNAKE3_BODY:
                    element = '&'
                    self.stdscr.addch(row_i, col_i, element, curses.color_pair(3))
                elif col == FRUIT:
                    element = 'O'
                    self.stdscr.addch(row_i, col_i, element, curses.color_pair(4))
                col_i += 2
            row_i += 1

        snake_i = 0
        for snake in self.snakes:
            self.stdscr.addstr(self.board.dimension + 1 + snake_i, 1, f"Snake {snake_i+1}: {snake.points}")
            self.stdscr.addstr(1 + snake_i, self.board.dimension*2 + 2, f"Snake {snake_i+1} pos: {snake.position[0].x}, {snake.position[0].y}") 
            snake_i += 1
        self.stdscr.refresh()