import settings
# import msvcrt as m

# from calculator import calculator
from components.dungeon import Dungeon

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

# calc = calculator.Calculator()
# # pprint.pprint(calculator)
# print(calc.multiply(5,3))

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

dungeon = Dungeon(width=parameters['width'], height=parameters['height'], enemies_number=parameters['enemies_number'])

horizontal_index = 3
vertical_index = 3

while key.lower() != 'q':
    # print('EXIT:  ', dungeon.exit.position)
    # print('YOU:   ', dungeon.character.position)
    # for enemy in canvas.enemies:
    #     print('ENEMY: ', enemy.position)
    # print('FIELD: ' + str(canvas.width) + ' X ' + str(canvas.height))
    # print('---------------------------------------------------')
    enemy_positions = [enemy.position for enemy in dungeon.enemies]
    map_list = []
    for y in range(0, dungeon.height):
        line = '|'
        for x in range(0, dungeon.width):
            position = [x, y]
            if position == dungeon.exit.position:
                line += 'E|'
            elif position == dungeon.character.position:
                line += 'C|'
            elif position in enemy_positions:
                line += 'X|'
            else:
                line += ' |'
        map_list.append(line)
    map_list = list(reversed(map_list))
    map_graph = '\n'.join(map_list)
    print(map_graph)

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

    dungeon.character.move(dungeon, direction=next_position)

    for enemy in dungeon.enemies:
        enemy.move(dungeon)
    win, lose = dungeon.check()
    if lose:
        message = 'You Lose!'
        break
    if win:
        message = 'You Win!'
        break
print(message)
