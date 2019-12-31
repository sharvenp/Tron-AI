
from settings import Settings

import time as t
import pygame as pg

class Tron:

    def __init__(self, players):

        self.players = players

        self.screen = pg.display.set_mode((Settings.DIMENSIONS, Settings.DIMENSIONS))    
        pg.display.set_caption("Tron")

        self.map = []

        for i in range(Settings.MAP_DIMENSIONS):
            a = []
            for j in range(Settings.MAP_DIMENSIONS):
                a.append(0)
            self.map.append(a)

    def _update_map(self):
        pass

    def _render_map(self):
        pass


    def run_game(self):

        game_over = False

        while not game_over:

            self._update_map()

            e = pg.event.poll()
            keys = key.get_pressed()
            if e.type == pg.QUIT: 
                quit(0)

            pg.display.update()