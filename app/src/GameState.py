from enum import Enum


class GameState(Enum):
    UNFINISHED = 0
    MAX_WIN = 1
    MIN_WIN = -1
