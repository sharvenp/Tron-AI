
from player import Player
from settings import Settings

class KeyBoardPlayer(Player):

    def __init__(self, color, start_pos, control_scheme):
        Player.__init__(self, color, start_pos)
        self.control_scheme = control_scheme

        self.direction = 0

    def move(self, e, keys):

        pass