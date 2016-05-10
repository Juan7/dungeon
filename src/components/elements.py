from random import randint

from .functions import apply_movement

class BaseElement():

    MOVEMENTS = {
        'LEFT': (-1, 0),
        'RIGHT': (1, 0),
        'UP': (0, -1),
        'DOWN': (0, 1),
    }
    position = (None, None)
    type = None

    def get_valid_movements(self, canvas):
        valid_movements = []
        if position.first() != 0:
            valid_movements.append('LEFT')
        if position.first() != canvas.width - 1:
            valid_movements.append('RIGHT')
        if position.second() != 0:
            valid_movements.append('UP')
        if position.second() != canvas.height - 1:
            valid_movements.append('DOWN')
        return valid_movements

    def apply_movement(self, pair):
        self.position = (position.first() + pair.first(), position.second() + pair.second())

    def set_new_position(self, choose):
        self.position = apply_movement(self, MOVEMENTS[choose])

    def move(self, direction=None):
        valid_movements = self.get_valid_movements()
        choose = randint(0,len(valid_movements))
        if direction:
            choose = valid_movements.index(direction)
        self.set_new_position(choose)

class Exit(BaseElement):
    type = 'exit'

    def move(self):
        pass


class Character(BaseElement):
    type = 'character'


class Enemy(BaseElement):
    type = 'enemy'
