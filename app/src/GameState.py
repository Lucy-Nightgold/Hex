from enum import Enum


class GameState(Enum):
    UNFINISHED = 0
    MAX_WINNER = 1
    MIN_WINNER = 2
