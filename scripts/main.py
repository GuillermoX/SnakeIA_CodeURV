import curses


from config import *
from game.snakeGame import SnakeGame

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

        game = SnakeGame(BOARD_DIM, msDelay,stdscr)
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
