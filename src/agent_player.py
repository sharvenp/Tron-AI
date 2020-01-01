
from player import Player
from agent import Agent

class AgentPlayer(Player, Agent):

    def __init__(self, color, start_pos, architecture, lr, gamma, saving_interval, load_most_recent, model_directory):
        Player.__init__(self, color, start_pos)
        Agent.__init__(self, architecture, lr, gamma, saving_interval, load_most_recent, model_directory)

    def move(self):
        pass