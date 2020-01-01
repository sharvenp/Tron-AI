
from player import Player
from agent import Agent
from settings import Settings

import math as m

class AgentPlayer(Player, Agent):

    def __init__(self, color, start_pos, architecture, lr, gamma, saving_interval, load_most_recent, model_directory):
        Player.__init__(self, color, start_pos)
        Agent.__init__(self, architecture, lr, gamma, saving_interval, load_most_recent, model_directory)

    def move(self, game_map, other_player_position):
        x = self._get_input_vector(game_map, other_player_position)
        action = self.get_state_action(x)

        if action == 0:
            self.direction = (-1, 0)
        elif action == 1:
            self.direction = (1, 0)
        elif action == 2:
            self.direction = (0, -1)
        elif action == 3:
            self.direction = (0, 1)

        return action

    def _cast_ray(self, direction, game_map):
        dr, dc = direction
        row, col = self.position
        curr_row, curr_col = row + dr, col + dc
        
        while (0 <= curr_row < Settings.MAP_DIMENSIONS) and (0 <= curr_col < Settings.MAP_DIMENSIONS):
            
            if game_map[curr_row][curr_col] != 0:
                break
            
            curr_row += dr
            curr_col += dc

        return curr_row, curr_col

    def _get_distance(self, row, col):
        curr_row, curr_col = self.position
        return m.sqrt((curr_row - row)**2 + (curr_col - col)**2)

    def _get_input_vector(self, game_map, other_player_position):

        # 8 Directions + Current Direction + Distance from opponent

        x = []
        row, col = self.position
        max_distance = m.sqrt(2 * (Settings.MAP_DIMENSIONS**2)) 

        # 8 directions of vision
        i = 0
        for dr in range(-1, 2):
            for dc in range(-1, 2):

                if dr == 0 and dc == 0:
                    continue

                cr, cc = self._cast_ray((dr, dc), game_map)
                d = self._get_distance(cr, cc)
                x.append(d / max_distance)
                i += 1

        dr, dc = self.direction
 
        # Current direction
        if dr == -1: # Up
            x.append(0.25)
        elif dc == -1: # Left
            x.append(0.5)     
        elif dr == 1: # Down
            x.append(0.75)
        elif dc == 1: # Right
            x.append(1)

        # Distance from opponent  
        orow, ocol = other_player_position
        d = self._get_distance(orow, ocol)
        x.append(d / max_distance)  

        return x



