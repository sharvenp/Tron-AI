

from settings import Settings
from agent_player import AgentPlayer

import time as t
import pygame as pg

class Tron_Trainer:

    def __init__(self, p1, p2):

        self.p1 = p1
        self.p2 = p2

        self.players = [p1, p2]

        self.screen = pg.display.set_mode((Settings.DIMENSIONS, Settings.DIMENSIONS))    
        pg.display.set_caption("Tron")

        self._reset_map()

    def _get_winners (self):
        if self.p1.is_dead and self.p2.is_dead:
            return [self.p1, self.p2]
        elif not (self.p1.is_dead or self.p2.is_dead):
            return None

        if self.p1.is_dead: return [self.p2]
        if self.p2.is_dead: return [self.p1]

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

        episode = self.p1.current_episode
        start_time = t.time()

        while True:
            
            self._reset_map()

            for player in self.players:
                player.reset()
            
            game_over = False

            self.p1.reset_training_data()
            self.p2.reset_training_data()

            while not game_over:

                e = pg.event.poll()
                if e.type == pg.QUIT: 
                    quit(0)
                
                for player in self.players:
                    if not player.is_dead:
                        other_player = None
                        if player == self.p1:
                            other_player = self.p2
                        else:
                            other_player = self.p1
                    
                        player.move(self.map, other_player.position)                    
                        player.update_position()

                self._update_map()
                self._render_map()
                pg.display.update()

                winner = self._get_winners() 
                game_over = (winner is not None)

                if game_over:
                    if len(winner) == 1 and winner[0] == self.p1:
                        self.p1.add_reward(Settings.REWARD_KILL)
                        self.p2.add_reward(Settings.REWARD_DEAD)
                    elif len(winner) == 1 and winner[0] == self.p2:
                        self.p2.add_reward(Settings.REWARD_KILL)
                        self.p1.add_reward(Settings.REWARD_DEAD)   
                    elif len(winner) == 2:
                        self.p1.add_reward(Settings.REWARD_DEAD)   
                        self.p2.add_reward(Settings.REWARD_DEAD)
                else:
                    self.p1.add_reward(Settings.REWARD_ALIVE)
                    self.p2.add_reward(Settings.REWARD_ALIVE)

                # t.sleep(Settings.BUFFER_DELAY)

            elapsed_time = t.time() - start_time    
            time_str = t.strftime("%H:%M:%S", t.gmtime(elapsed_time))  
            episode += 1

            for i in range(len(self.players)):

                if self.players[i] in winner:
                    self.players[i].add_point()

                output_string = "Player {}- Episode: {:0>5} Score: {:0>3} Reward: {:0>7} T+: {}".format(i+1, episode, self.players[i].score, sum(self.players[i].rewards), time_str)
                self.players[i].train_wrapper(episode)
                print(output_string)
