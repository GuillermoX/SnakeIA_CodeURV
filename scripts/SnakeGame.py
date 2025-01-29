import random
import curses

keysPressed = set()
stdscr = None

EMPTY = 0
SNAKE1_HEAD = 1
SNAKE1_BODY = 2
SNAKE2_HEAD = 3     #FOR FUTURE 2 SNAKE GAMES
SNAKE2_BODY = 4
SNAKE3_HEAD = 5
SNAKE3_BODY = 6
FRUIT = -1

"""
def on_press(key):
    try:
        keysPressed.add(key.char)
    except AttributeError:
        keysPressed.add(str(key))

def on_release(key):
    try:
        keysPressed.discard(key.char)
    except AttributeError:
        keysPressed.discard(str(key))


listener = keyboard.Listener(on_press=on_press, on_release=on_release, suppress=True)
listener.start()
"""


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

class Board:
    def __init__(self, dimension: int):
        self.dimension = dimension
        self.boxes = [[EMPTY]*self.dimension for _ in range(self.dimension)]

    def setElementPos(self, element: int, position: Vect2d):
        self.boxes[position.y][position.x] = element


class Snake:

    def __init__(self, ia):
        self.position = [Vect2d(0,0)]       #Position of each part of the body (first is head)
        self.dir = Vect2d(1,0)              #Direction of the head
        self.lenght = 0
        self.vel = 1
        self.points = 0
        self.alive = True
        self.ia = ia                        #Specify if the snake is going to be controlled by IA of human
    
    def incrementLenght(self, incremenet: int):
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

    def choseDirection(self, keysPressed, fruits, dim):
        #TODO: If the snake is controlled by AI let the AI decide
        
        if(self.ia): 
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
            
                
        else:
            if ord('d') in keysPressed and self.dir.x == 0:
                self.dir = Vect2d(1,0)
            if ord('a') in keysPressed and self.dir.x == 0:
                self.dir = Vect2d(-1,0)
            if ord('w') in keysPressed and self.dir.y == 0: 
                self.dir = Vect2d(0,-1)
            if ord('s') in keysPressed and self.dir.y == 0: 
                self.dir = Vect2d(0,1)

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


class Fruit:
    def __init__(self, pos: Vect2d, points: int):
        self.pos = pos
        self.points = points
            

    
    
    

class SnakeGame:

    def __init__(self, dim, msDelay):
        self.gameRunning = False
        self.board = Board(dim)
        self.snakes = [Snake(False), Snake(True)]
        self.numSnakes = 1
        self.keysPressed = set()
        self.fruits = []
        self.msDelay = msDelay

    def checkGame(self, snake):
            if snake.isOutOfBoard(self.board.dimension):
                self.gameRunning = False
                snake.alive = False
                

            #TODO: Check if the snake head has crashed his own body

    def initSnakes(self):
        for snake in self.snakes:
            snake.position[0].x = random.randint(1, self.board.dimension-2)
            snake.position[0].y = random.randint(1, self.board.dimension-2)

    def getKeys(self):
        global stdscr
        keys = stdscr.getch()
        if keys != -1 and not(keys in self.keysPressed):
            self.keysPressed.add(keys)
        else:
            self.keysPressed.clear()

    def generateFruit(self):
        randomPos = Vect2d(random.randint(0, self.board.dimension-1), random.randint(0, self.board.dimension-1))
        newFruit = Fruit(randomPos, 10)
        self.fruits.append(newFruit)

    def runGame(self):
        self.gameRunning = True
        self.initSnakes()
        timeCount = 0

        while self.gameRunning:
            self.getKeys() 

            if(timeCount >= 1*(1000/self.msDelay)):
                timeCount = 0
                self.generateFruit()

            for snake in self.snakes:
                snake.choseDirection(self.keysPressed, self.fruits, self.board.dimension)
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
        global stdscr
        stdscr.clear()
        row_i = 0
        for row in self.board.boxes:
            col_i = 0
            for col in row:
                element = '0'
                if col == EMPTY:
                    element = '·'
                    stdscr.addch(row_i, col_i, element)
                elif col == SNAKE1_HEAD:
                    element = '@'
                    stdscr.addch(row_i, col_i, element, curses.color_pair(1))
                elif col == SNAKE1_BODY:
                    element = '#'
                    stdscr.addch(row_i, col_i, element, curses.color_pair(1))
                elif col == SNAKE2_HEAD:
                    element = '&'
                    stdscr.addch(row_i, col_i, element, curses.color_pair(2))
                elif col == SNAKE2_BODY:
                    element = '$' 
                    stdscr.addch(row_i, col_i, element, curses.color_pair(2))
                elif col == SNAKE3_HEAD:
                    element = '%'
                    stdscr.addch(row_i, col_i, element, curses.color_pair(3))
                elif col == SNAKE3_BODY:
                    element = '&'
                    stdscr.addch(row_i, col_i, element, curses.color_pair(3))
                elif col == FRUIT:
                    element = 'O'
                    stdscr.addch(row_i, col_i, element, curses.color_pair(4))
                col_i += 2
            row_i += 1

        snake_i = 0
        for snake in self.snakes:
            stdscr.addstr(self.board.dimension + 1 + snake_i, 1, f"Snake {snake_i+1}: {snake.points}")
            stdscr.addstr(1 + snake_i, self.board.dimension*2 + 2, f"Snake {snake_i+1} pos: {snake.position[0].x}, {snake.position[0].y}") 
            snake_i += 1
        stdscr.refresh()

                
        


def main(stdscr_local):
    global stdscr
    stdscr = stdscr_local
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)



    replay = True
    while replay:
        stdscr.nodelay(1)
        msDelay = 150
        stdscr.timeout(msDelay)

        height, width = stdscr.getmaxyx()

        game = SnakeGame(15, msDelay)
        game.runGame()

        printGameOver(game)

        keyIncorrect = True
        while keyIncorrect:
            stdscr.nodelay(0)
            key = stdscr.getch()
            if key == ord('Q') or key == ord('q'):
                keyIncorrect = False
                replay = False
            elif key == ord('R') or key == ord('r'):
                keyIncorrect = False
                replay = True

def printGameOver(game):
    snake_i = 1
    for snake in game.snakes:
        if(not(snake.alive)):
            break
        snake_i += 1

    stdscr.addstr(game.board.dimension + 5, 1, f"GAME OVER -> Snake {snake_i} died")
    stdscr.addstr(game.board.dimension + 6, 1, "- Press R to Restart")
    stdscr.addstr(game.board.dimension + 7, 1, "- Press Q to Quit")
    

curses.wrapper(main)