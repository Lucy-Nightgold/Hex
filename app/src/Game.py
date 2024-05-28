from src.Algorithms import minimax, alphabeta
from src.GameState import GameState
from src.datastructure.HexConstants import NODE_STATE_EMPTY
from src.datastructure.TreeManager import generate_tree, is_winning


class Game:

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.state = GameState.UNFINISHED
        self.tree = generate_tree(difficulty.value)

    def play_turn(self, player_action):
        if self.state != GameState.UNFINISHED:
            raise Exception("game already finished")
        old_state = self.tree.root.state
        if old_state[player_action] != NODE_STATE_EMPTY:
            raise Exception("space already occupied")
        new_state = old_state[:player_action] + 'M' + old_state[player_action + 1:]
        self.tree.select_next_root(new_state)
        if is_winning(new_state) == GameState.MAX_WIN:
            return GameState.MAX_WIN
        self.tree.expend()
        min_h = float('inf')
        min_node = self.tree.root.successors[0]
        for n in self.tree.root.successors:
            res = alphabeta(n)
            if res <= min_h:
                min_h = res
                min_node = n
        self.tree.root = min_node
        self.tree.expend()
        win = self.tree.is_winning()
        self.state = win
        return win
