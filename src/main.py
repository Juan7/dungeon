import curses

from components.dungeon import *

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

key = ''
win = False
canvas = Canvas()
while key != ord('q') or not win:
    key = stdscr.getch()
    # stdscr.addch(20,25,key)
    stdscr.refresh()

    stdscr.addstr(2, 20, canvas.exit.position)
    stdscr.addstr(3, 20, canvas.character.position)
    stdscr.addstr(4, 20, "--------------- Enemies ---------------")
    x = 5
    for enemy in canvas.enemies:
        stdscr.addstr(x, 20, canvas.exit.position)
        x += 1

    next_position = ''
    if key == curses.KEY_UP:
        next_position('UP')
    elif key == curses.KEY_DOWN:
        next_position('DOWN')
    elif key == curses.KEY_LEFT:
        next_position('LEFT')
    elif key == curses.KEY_RIGHT:
        next_position('RIGHT')

    canvas.character.move(next_position)
    for enemy in canvas.enemies:
        enemy.move()
    win, lose = canvas.check()
    if lose:
        stdscr.addstr(1, 20, "You Lose")
        curses.endwin()
stdscr.addstr(0, 20, "You Win!")
curses.endwin()
