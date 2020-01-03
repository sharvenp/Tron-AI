
from tron_trainer import Tron_Trainer
from agent_player import AgentPlayer

import pygame as pg

if __name__ == "__main__":
    
    architecture = [(10, ''), (7, 'relu'), (7, 'relu'), (4, 'softmax')]

    agent_1 = AgentPlayer((255, 0, 255), (50, 10), architecture, 0.0008, 0.99, 1000, False, 'models/1')
    agent_2 = AgentPlayer((0, 255, 255), (50, 90), architecture, 0.0008, 0.99, 1000, False, 'models/2')

    t = Tron_Trainer(agent_1, agent_2)
    t.run_game()