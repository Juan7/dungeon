import curses
# import msvcrt as m

from components.dungeon import *

# stdscr = curses.initscr()
# curses.cbreak()
# stdscr.keypad(True)
#
# stdscr.addstr(0,0,"Hit 'q' to quit")
# stdscr.refresh()

key = ''
win = False
canvas = Canvas()
for enemy_number in range(canvas.enemies_number):
    enemy = Enemy()
    enemy.start_position(canvas)
    canvas.enemies.append(enemy)

character = Character()
character.start_position(canvas)
canvas.character = character

exit = Exit()
exit.start_position(canvas)
canvas.exit = exit

horizontal_index = 3
vertical_index = 3

while key != ord('q') or not win:
    print("EXIT: %s", canvas.exit.position)
    print("YOU:  %s", canvas.character.position)
    # stdscr.addstr(vertical_index, 3, "EXIT: " + str(canvas.exit.position))
    # vertical_index += 3
    # stdscr.addstr(vertical_index, 3, "YOU:  " + str(canvas.character.position))
    # vertical_index += 3
    for enemy in canvas.enemies:
        print("ENEMY: %s", enemy.position)
        # stdscr.addstr(vertical_index, 3, "ENEMY: " + str(enemy.position))
        # vertical_index += 3
    print("FIELD: " + str(canvas.width) + " X " + str(canvas.height))
    print("---------------------------------------------------")
    # stdscr.addstr(vertical_index, 3, "FIELD: " + str(canvas.width) + " X " + str(canvas.height))
    # vertical_index += 3
    # stdscr.addstr(vertical_index, 3, "---------------------------------------------------")
    # vertical_index += 3
    # key = m.getch()
    key = input()
    # stdscr.addch(20,25,key)
    # stdscr.refresh()

    # stdscr.addstr(2, 20, canvas.exit.position)
    # stdscr.addstr(3, 20, canvas.character.position)
    # stdscr.addstr(4, 20, "--------------- Enemies ---------------")
    # x = 5
    #
    # for enemy in canvas.enemies:
    #     stdscr.addstr(x, 20, canvas.exit.position)
    #     x += 1
    print(key)
    next_position = ''
    if key == curses.KEY_UP:
        next_position = 'UP'
    elif key == curses.KEY_DOWN:
        next_position = 'DOWN'
    elif key == curses.KEY_LEFT:
        next_position = 'LEFT'
    elif key == curses.KEY_RIGHT:
        next_position = 'RIGHT'

    canvas.character.move(canvas, next_position)

    for enemy in canvas.enemies:
        enemy.move(canvas)
    win, lose = canvas.check()
    if lose:
        print("You Lose")
        # stdscr.addstr(1, 20, "You Lose")
        # curses.endwin()
print("You win!")
# stdscr.addstr(0, 20, "You Win!")
# curses.endwin()
