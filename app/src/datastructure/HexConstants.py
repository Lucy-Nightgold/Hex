MAX_START = range(0, 10)
MIN_START = [0, 11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
MAX_STOP = range(110, 120)
MIN_STOP = [10, 21, 32, 43, 54, 65, 76, 87, 98, 109, 120]
CASES = range(0, 120)
CASES_NB = 121
NODE_STATE_MAX = 'M'
NODE_STATE_MIN = 'm'
NODE_STATE_EMPTY = '_'
MAX_WIN = 1
MIN_WIN = -1
UNFINISHED = 0


def get_neighbours(c):
    if c not in CASES:
        raise Exception("case out of bound")
    res = []
    if c not in MAX_START:
        res.extend(c - 11)
    if c not in MIN_STOP and c not in MAX_START:
        res.append(c - 10)
    if c not in MIN_START:
        res.append(c - 1)
    if c not in MIN_STOP:
        res.append(c + 1)
    if c not in MIN_START and c not in MAX_STOP:
        res.append(c + 10)
    if c not in MAX_STOP:
        res.append(c + 11)
    return res
