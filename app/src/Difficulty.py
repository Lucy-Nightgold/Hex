from enum import Enum


def get_difficulty_by_number(number):
    match number:
        case 2:
            return Difficulty.EASY
        case 4:
            return Difficulty.MEDIUM
        case 6:
            return Difficulty.HARD
        case _:
            return Difficulty.EASY


class Difficulty(Enum):
    EASY = 2
    MEDIUM = 4
    HARD = 6
