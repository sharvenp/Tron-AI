
class Settings:

    # Window params
    DIMENSIONS = 500

    # Map params
    MAP_DIMENSIONS = 100
    CELL_WIDTH = DIMENSIONS // MAP_DIMENSIONS

    # Loop delay (Controls speed of game)
    BUFFER_DELAY = 1/25

    # Colors
    BACKGROUND_COLOR = (0, 0, 0)

    # Rewards For Agents
    REWARD_ALIVE = 6
    REWARD_DEAD = -200
    REWARD_ALIVE_BONUS = 200
    REWARD_KILL = 500

    # Misc
    PRINT_INTERVAL = 100