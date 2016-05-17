import curses
# import msvcrt as m

from components.dungeon import *

print('---------------------------------------------------')
print('--                DUNGEON v1.0                   --')
print('---------------------------------------------------')
print('-- By: Phinxk                                    --')
print('-- AQP - 2016                                    --')
print('---------------------------------------------------')
print('-- KEYS:                                         --')
print('-- W: For UP                                     --')
print('-- S: For DOWN                                   --')
print('-- A: For LEFT                                   --')
print('-- D: For RIGHT                                  --')
print('-- FIND THE EXIT BEFORE THE ENEMIES FIND YOU!!!  --')
print('---------------------------------------------------')
print('---------------------------------------------------')


key = ''
message = ''
win = False
canvas = Canvas(width=10, height=10, enemies_number=2)
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

while key != ord('q'):
    print('EXIT: ', canvas.exit.position)
    print('YOU:  ', canvas.character.position)
    for enemy in canvas.enemies:
        print('ENEMY: ', enemy.position)
    print('FIELD: ' + str(canvas.width) + ' X ' + str(canvas.height))
    print('---------------------------------------------------')
    next_position = ''
    key = input()
    if key.lower() == 'w':
        next_position = 'UP'
    elif key.lower() == 's':
        next_position = 'DOWN'
    elif key.lower() == 'a':
        next_position = 'LEFT'
    elif key.lower() == 'd':
        next_position = 'RIGHT'

    # Must be set on keys
    # if key == curses.KEY_UP:
    #     next_position = 'UP'
    # elif key == curses.KEY_DOWN:
    #     next_position = 'DOWN'
    # elif key == curses.KEY_LEFT:
    #     next_position = 'LEFT'
    # elif key == curses.KEY_RIGHT:
    #     next_position = 'RIGHT'

    canvas.character.move(canvas, direction=next_position)

    for enemy in canvas.enemies:
        enemy.move(canvas)
    win, lose = canvas.check()
    if lose:
        message = 'You Lose!'
        break
    if win:
        message = 'You Win!'
        break
print(message)
