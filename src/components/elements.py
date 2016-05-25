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

    def start_position(self, dungeon):
        self.position = [randint(0, dungeon.width-1), randint(0, dungeon.height-1)]
        dungeon.matrix[self.position[0]][self.position[1]] = self

    def get_valid_movements(self, dungeon):
        valid_movements = []
        if self.position[0] != 0:
            valid_movements.append('LEFT')
        if self.position[0] != dungeon.width - 1:
            valid_movements.append('RIGHT')
        if self.position[1] != 0:
            valid_movements.append('DOWN')
        if self.position[1] != dungeon.height - 1:
            valid_movements.append('UP')
        return valid_movements

    def apply_movement(self, pair):
        self.position[0] += pair[0]
        self.position[1] += pair[1]

    def set_new_position(self, choose):
        self.apply_movement(self.MOVEMENTS[choose])

    def move(self, dungeon, direction=None):
        valid_movements = self.get_valid_movements(dungeon)
        if direction and self.type == 'character':
            try:
                choose = valid_movements.index(direction)
                self.set_new_position(valid_movements[choose])
                dungeon.matrix[self.position[0]][self.position[1]] = self
            except:
                pass
        if not direction and self.type == 'enemy':
            choose = randint(1,len(valid_movements))
            self.set_new_position(valid_movements[choose-1])
            dungeon.matrix[self.position[0]][self.position[1]] = self

        return self

class Exit(BaseElement):
    type = 'exit'
    graph = 'X|'

    def move(self, dungeon):
        dungeon.matrix[self.position[0]][self.position[1]] = self


class Character(BaseElement):
    type = 'character'
    graph = 'C|'


class Enemy(BaseElement):
    type = 'enemy'
    graph = 'E|'
