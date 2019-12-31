
from player import Player
from settings import Settings

import pygame as pg

class KeyBoardPlayer(Player):

    def __init__(self, color, start_pos, control_scheme):
        Player.__init__(self, color, start_pos)
        self.control_scheme = control_scheme

    def move(self, e, keys):

        if e.type == pg.KEYDOWN:

            if keys[self.control_scheme["UP"]]:
                self.direction = (-1, 0)
            elif keys[self.control_scheme["DOWN"]]:
                self.direction = (1, 0)
            elif keys[self.control_scheme["LEFT"]]:
                self.direction = (0, -1)
            elif keys[self.control_scheme["RIGHT"]]:
                self.direction = (0, 1)

    def update_position(self):

        row, col = self.position
        dr, dc = self.direction

        self.position = (row + dr, col + dc)