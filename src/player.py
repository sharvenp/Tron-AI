
class Player:

    def __init__(self, color, number, start_pos):
        self.color = color
        self.number = number
        self.start_pos = start_pos
        self.reset()

    def move(self, keys):
        raise NotImplementedError

    def reset(self):
        self.position = self.start_pos
        self.direction = (1, 0)
        self.is_dead = False

    def set_dead(self):
        self.is_dead = True
        self.direction = (0, 0)