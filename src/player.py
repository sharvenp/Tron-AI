
class Player:

    def __init__(self, color, start_pos):
        self.color = color
        self.start_pos = start_pos
        self.score = 0
        self.reset()

    def move(self, keys):
        raise NotImplementedError

    def add_point(self):
        self.score += 1

    def reset(self):
        self.position = self.start_pos
        self.direction = (1, 0)
        self.is_dead = False

    def set_dead(self):
        self.is_dead = True
        self.direction = (0, 0)