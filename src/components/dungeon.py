"""Contains all the methods and elements for the area of game."""

import settings

from .elements import Enemy, Character, Exit
from .functions import set_field

class Dungeon():
    """Set the current area of game."""

    width = None
    height = None
    enemies_number = None
    enemies = []
    character = None
    exit = None
    matrix = []

    def __init__(self, width=5, height=5, enemies_number=1):
        """Init the values for Dungeon."""
        self.width = width
        self.height = height
        self.enemies_number = enemies_number
        self.matrix = set_field(self.width, self.height)

        del self.enemies[:]
        for enemy_number in range(self.enemies_number):
            enemy = Enemy()
            enemy.start_position(dungeon=self)
            self.enemies.append(enemy)

        self.character = Character()
        self.character.start_position(dungeon=self)

        self.exit = Exit()
        self.exit.start_position(dungeon=self)

        need_repositions = self.repositions()
        while need_repositions:
            need_repositions = self.repositions()

    def check(self):
        """Check if the game continue or is a win/lose."""
        win = self.exit.position == self.character.position
        lose = any(self.character.position == enemy.position for enemy in self.enemies)
        return win, lose

    def repositions(self):
        """Recalculate the position of character and exit to avoid bad startings."""
        instant_win = self.character.position == self.exit.position
        instant_lose_or_enemy_exit = any(
                                        self.character.position == enemy.position
                                        or self.exit.position == enemy.position
                                        for enemy in self.enemies
                                    )
        need_reposition = instant_lose_or_enemy_exit or instant_win
        if need_reposition:
            self.matrix[self.character.position[0]][self.character.position[1]] = None
            self.matrix[self.exit.position[0]][self.exit.position[1]] = None
            self.character.start_position(dungeon=self)
            self.exit.start_position(dungeon=self)
        return need_reposition

    def next_move(self, direction):
        """Makes the next move for all the dungeon elements."""
        self.matrix = set_field(self.width, self.height)
        self.exit.move(dungeon=self)
        self.character.move(dungeon=self, direction=direction)
        win, lose = self.check()
        if lose:
            return win, lose
        for enemy in self.enemies:
            enemy.move(dungeon=self)
        win, lose = self.check()
        return win, lose

    def dungeon_as_str(self):
        """Return the dungeon map as an string for print."""
        enemy_positions = [enemy.position for enemy in self.enemies]
        map_list = []
        for y in range(0, self.height):
            line = '|'
            for x in range(0, self.width):
                line += self.matrix[x][y].graph if self.matrix[x][y] else ' |'
            map_list.append(line)
        map_list = list(reversed(map_list))
        map_graph = '\n'.join(map_list)
        return map_graph
