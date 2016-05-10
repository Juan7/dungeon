"""Contains all the methos and elements for the area of game."""

import settings

from .functions import set_field

class Canvas():
    """Set the current area of game."""

    width = None
    height = None
    enemies_number = None
    enemies = []
    character = None
    exit = None
    matrix = []

    def __init__(self, width=5, height=5, enemies_number=1):
        self.width = width
        self.height = height
        self.enemies_number = enemies_number

        for enemy_number in self.enemies_number:
            enemy = Enemy()
            enemy.start_position(self)
            self.enemies.append(enemy)

        self.character = Character().start_position(self)
        self.exit = Exit().start_position(self)

        set_field(self.matrix, self.width, self.height)


    def check(self):
        win = False
        lose = False
        if self.exit.position == self.character.position:
            win = True
        for enemy in self.enemies:
            if self.character.position == enemy.position:
                lose = True
                break
        return win, lose
