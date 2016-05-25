import settings
# import msvcrt as m

from calculator import calculator
import pprint
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
print('--              Press Q for Quit!!!              --')
print('---------------------------------------------------')

calc = calculator.Calculator()
# pprint.pprint(calculator)
print(calc.multiply(5,3))

key = ''
message = 'Thanks for playing!'
win = False

parameters = {
    'width' : settings.DEFAULT_WIDTH,
    'height' : settings.DEFAULT_HEIGHT,
    'enemies_number' : settings.DEFAULT_ENEMIES,
}

print('--      Do you wanna config your game?  y/n      --')
key = input()

if key.lower() == 'y':
    for parameter in settings.PARAMETERS:
        for index, value in parameter.items():  # Loop over 1 key dictionary
            print(value['message'])
            key = input()
            while not key.strip().isdigit() or int(key.strip()) > value['max']:
                print(value['ex_message'])
                key = input()
            parameters[index] = int(key.strip())

canvas = Canvas(width=parameters['width'], height=parameters['height'], enemies_number=parameters['enemies_number'])

horizontal_index = 3
vertical_index = 3

while key.lower() != 'q':
    print('EXIT:  ', canvas.exit.position)
    print('YOU:   ', canvas.character.position)
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
