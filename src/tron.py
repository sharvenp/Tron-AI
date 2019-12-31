
from settings import Settings

import time as t
import pygame as pg

class Tron:

    def __init__(self, players):

        self.players = players

        self.screen = pg.display.set_mode((Settings.DIMENSIONS, Settings.DIMENSIONS))    
        pg.display.set_caption("Tron")

        self._reset_map()

    def _get_player_count(self):
        count = 0
        for player in self.players:
            count += int(not player.is_dead)
        return count

    def _get_player(self, number):
        for player in self.players:
            if player.number == number:
                return player

    def _check_in_bounds(self, row, col):
        return (0 <= row < Settings.MAP_DIMENSIONS) and (0 <= col < Settings.MAP_DIMENSIONS)

    def _update_map(self):
        
        for player in self.players:
            row, col = player.position 

            if not self._check_in_bounds(row, col):
                player.set_dead()
                continue

            if self.map[row][col] != 0:
                player.set_dead()
                continue

            self.map[row][col] = player.number

    def _render_map(self):

        self.screen.fill(Settings.BACKGROUND_COLOR)
        
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                number = self.map[row][col]
                if number:
                    color = self._get_player(number).color
                    pg.draw.rect(self.screen, color, (col * Settings.CELL_WIDTH, row * Settings.CELL_WIDTH, Settings.CELL_WIDTH, Settings.CELL_WIDTH))

    def _reset_map(self):
        self.map = []
        for i in range(Settings.MAP_DIMENSIONS):
            a = []
            for j in range(Settings.MAP_DIMENSIONS):
                a.append(0)
            self.map.append(a)

    def run_game(self):

        while True:

            for player in self.players:
                player.reset()
                self._reset_map()
            
            game_over = False

            while not game_over:
                
                game_over = (self._get_player_count() <= 1)

                e = pg.event.poll()
                if e.type == pg.QUIT: 
                    quit(0)
                
                keys = pg.key.get_pressed()

                for player in self.players:
                    if not player.is_dead:
                        player.move(e, keys)
                        player.update_position()

                self._update_map()
                self._render_map()
                pg.display.update()

                t.sleep(Settings.BUFFER_DELAY)

            print("Crashed")