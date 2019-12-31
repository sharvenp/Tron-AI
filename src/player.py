
class Player:

    def __init__(self, color, start_pos):
        self.color = color
        self.position = start_pos

    def move(self, keys):
        raise NotImplementedError