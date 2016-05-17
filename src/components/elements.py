from random import randint

class BaseElement():

    MOVEMENTS = {
        'LEFT': [-1, 0],
        'RIGHT': [1, 0],
        'UP': [0, 1],
        'DOWN': [0, -1],
    }
    position = [None, None]
    type = None

    def start_position(self, canvas):
        self.position = [randint(0,canvas.width-1), randint(0,canvas.height-1)]

    def get_valid_movements(self, canvas):
        valid_movements = []
        if self.position[0] != 0:
            valid_movements.append('LEFT')
        if self.position[0] != canvas.width - 1:
            valid_movements.append('RIGHT')
        if self.position[1] != 0:
            valid_movements.append('DOWN')
        if self.position[1] != canvas.height - 1:
            valid_movements.append('UP')
        return valid_movements

    def apply_movement(self, pair):
        self.position[0] += pair[0]
        self.position[1] += pair[1]

    def set_new_position(self, choose):
        self.apply_movement(self.MOVEMENTS[choose])

    def move(self, canvas, direction=None):
        valid_movements = self.get_valid_movements(canvas)
        if direction and self.type == 'character':
            try:
                choose = valid_movements.index(direction)
                self.set_new_position(valid_movements[choose])
            except:
                pass
        if not direction and self.type == 'enemy':
            choose = randint(1,len(valid_movements))
            self.set_new_position(valid_movements[choose-1])
        return self

class Exit(BaseElement):
    type = 'exit'

    def move(self):
        pass


class Character(BaseElement):
    type = 'character'


class Enemy(BaseElement):
    type = 'enemy'
