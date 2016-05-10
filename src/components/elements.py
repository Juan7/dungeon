from random import randint

class BaseElement():

    MOVEMENTS = {
        'LEFT': [-1, 0],
        'RIGHT': [1, 0],
        'UP': [0, -1],
        'DOWN': [0, 1],
    }
    position = [None, None]
    type = None

    def start_position(self, canvas):
        self.position = [randint(0,canvas.width), randint(0,canvas.height)]

    def get_valid_movements(self, canvas):
        valid_movements = []
        if self.position[0] != 0:
            valid_movements.append('LEFT')
        if self.position[0] != canvas.width - 1:
            valid_movements.append('RIGHT')
        if self.position[1] != 0:
            valid_movements.append('UP')
        if self.position[1] != canvas.height - 1:
            valid_movements.append('DOWN')
        return valid_movements

    def apply_movement(self, pair):
        print(self.type)
        print("Your position is %s", self.position)
        self.position[0] += pair[0]
        self.position[1] += pair[1]
        print("Your NEW position is %s", self.position)

    def set_new_position(self, choose):
        self.apply_movement(self.MOVEMENTS[choose])

    def move(self, canvas, direction=None):
        valid_movements = self.get_valid_movements(canvas)
        choose = randint(0,len(valid_movements))
        if direction:
            try:
                choose = valid_movements.index(direction)
            except:
                pass
        self.set_new_position(valid_movements[choose])
        return self

class Exit(BaseElement):
    type = 'exit'

    def move(self):
        pass


class Character(BaseElement):
    type = 'character'


class Enemy(BaseElement):
    type = 'enemy'
