
from tron import Tron
from keyboard_player import KeyBoardPlayer

import pygame as pg

if __name__ == "__main__":

    p1_control_scheme = {"UP":pg.K_w, "DOWN":pg.K_s, "LEFT":pg.K_a, "RIGHT":pg.K_d}
    p1 = KeyBoardPlayer((255, 0, 0), (25, 50), p1_control_scheme)

    p2_control_scheme = {"UP":pg.K_UP, "DOWN":pg.K_DOWN, "LEFT":pg.K_LEFT, "RIGHT":pg.K_RIGHT}
    p2 = KeyBoardPlayer((0, 255, 0), (75, 50), p2_control_scheme)

    t = Tron([p1, p2])
    t.run_game()