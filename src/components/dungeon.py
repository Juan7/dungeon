"""Contains all the methos and elements for the area of game."""

import settings

from .functions import set_field

class Canvas():
    """Set the current area of game."""
    
    width = None
    height = None
    enemies = None
    matrix = []
    
    def __init__(self, width=5, height=5, enemies=1):
        self.width = width
        self.height = height
        self.enemies = enemies
        set_field(self.matrix, self.width, self.height)
    
    