
from settings import Settings
from keyboard_player import KeyBoardPlayer

import time as t
import pygame as pg

class Tron:

    def __init__(self, players):

        self.players = players

        self.screen = pg.display.set_mode((Settings.DIMENSIONS, Settings.DIMENSIONS))    
        pg.display.set_caption("Tron")

        self._reset_map()

    def _get_winner (self):
        alive = []
        dead = []
        for player in self.players:
            if player.is_dead:
                dead.append(player)
            else:
                alive.append(player)

        if len(alive) == 1:
            return alive

        if len(alive) == 0:
            return dead
        
        return None

    def _check_in_bounds(self, row, col):
        return (0 <= row < Settings.MAP_DIMENSIONS) and (0 <= col < Settings.MAP_DIMENSIONS)

    def _update_map(self):
        
        for i in range(len(self.players)):
            row, col = self.players[i].position 

            if not self._check_in_bounds(row, col):
                self.players[i].set_dead()
                continue

            if self.map[row][col] != 0:
                self.players[i].set_dead()
                continue

            self.map[row][col] = i + 1

    def _render_map(self):

        self.screen.fill(Settings.BACKGROUND_COLOR)
        
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                number = self.map[row][col]
                if number:
                    color = self.players[number - 1].color
                    pg.draw.rect(self.screen, color, (col * Settings.CELL_WIDTH, row * Settings.CELL_WIDTH, Settings.CELL_WIDTH, Settings.CELL_WIDTH))

    def _reset_map(self):
        self.map = []
        for i in range(Settings.MAP_DIMENSIONS):
            a = []
            for j in range(Settings.MAP_DIMENSIONS):
                a.append(0)
            self.map.append(a)

    def _get_agent_input(self, number):
        pass

    def run_game(self):

        while True:

            for player in self.players:
                player.reset()
                self._reset_map()
            
            game_over = False

            while not game_over:
                
                winner = self._get_winner() 
                game_over = (winner is not None)

                e = pg.event.poll()
                if e.type == pg.QUIT: 
                    quit(0)
                
                for player in self.players:
                    if not player.is_dead:
                        player.move()
                        player.update_position()

                self._update_map()
                self._render_map()
                pg.display.update()

                t.sleep(Settings.BUFFER_DELAY)

            print("Game Over")
            for player in winner:
                player.add_point()
            for i in range(len(self.players)):
                print(f"Player {i + 1}: {self.players[i].score}")