class Node:
    def __init__(self, is_max, is_leaf, e, pred, state):
        self.is_max = is_max
        self.is_leaf = is_leaf
        self.is_ending = False
        self.e = e
        self.pred = pred
        self.state = state
        self.successors = []
