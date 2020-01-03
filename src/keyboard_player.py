
from player import Player
from settings import Settings

import pygame as pg

class KeyBoardPlayer(Player):

    def __init__(self, color, start_pos, start_direction, control_scheme):
        Player.__init__(self, color, start_pos, start_direction)
        self.control_scheme = control_scheme

    def move(self):

        keys = pg.key.get_pressed()
        if keys[self.control_scheme["UP"]]:
            self.direction = (-1, 0)
        elif keys[self.control_scheme["DOWN"]]:
            self.direction = (1, 0)
        elif keys[self.control_scheme["LEFT"]]:
            self.direction = (0, -1)
        elif keys[self.control_scheme["RIGHT"]]:
            self.direction = (0, 1)
