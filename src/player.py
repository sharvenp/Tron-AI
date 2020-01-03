
class Player:

    def __init__(self, color, start_pos, start_direction):
        self.color = color
        self.start_pos = start_pos
        self.start_direction = start_direction
        self.score = 0
        self.reset()

    def move(self, keys):
        raise NotImplementedError

    def add_point(self):
        self.score += 1

    def reset(self):
        self.position = self.start_pos
        self.direction = self.start_direction
        self.is_dead = False
        self.is_killed = False

    def set_dead(self):
        self.is_dead = True
        self.direction = (0, 0)

    def set_killed(self):
        self.is_killed = True
        self.direction = (0, 0)

    def update_position(self):

        row, col = self.position
        dr, dc = self.direction

        self.position = (row + dr, col + dc)