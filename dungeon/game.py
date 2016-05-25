from dungeon.settings import DEFAULT_ENEMIES, DEFAULT_HEIGHT, DEFAULT_WIDTH

from dungeon.components.dungeon import Dungeon


def start():
    parameters = {
        'width' : DEFAULT_WIDTH,
        'height' : DEFAULT_HEIGHT,
        'enemies_number' : DEFAULT_ENEMIES,
    }
    dungeon = Dungeon(width=parameters['width'], height=parameters['height'], enemies_number=parameters['enemies_number'])
    return dungeon
    # win = False
    # lose = False
    # message = 'Thanks for playing!'
    # while True:
    #     print(dungeon.dungeon_as_str())
    #
    #     next_position = ''
    #     key = input()
    #     if key.lower() == settings.MOVE_UP:
    #         next_position = 'UP'
    #     elif key.lower() == settings.MOVE_DOWN:
    #         next_position = 'DOWN'
    #     elif key.lower() == settings.MOVE_LEFT:
    #         next_position = 'LEFT'
    #     elif key.lower() == settings.MOVE_RIGHT:
    #         next_position = 'RIGHT'
    #
    #     win, lose = dungeon.next_move(direction=next_position)
    #     # win, lose = dungeon.check()
    #     if lose:
    #         message = 'You Lose!'
    #         break
    #     if win:
    #         message = 'You Win!'
    #         break
    # print(message)

if __name__ == "__main__":
    start()
