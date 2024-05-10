from app.src.GameState import GameState
from app.src.datastructure.HexConstants import NODE_STATE_EMPTY, MAX_WIN
from app.src.datastructure.TreeManager import generate_tree, is_winning


class Game:

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.state = GameState.UNFINISHED
        self.tree = generate_tree(difficulty.value)

    def play_turn(self, player_action):
        old_state = self.tree.root.state
        if old_state[player_action] != NODE_STATE_EMPTY:
            raise Exception("space already occupied")
        new_state = old_state[:player_action] + player_action + old_state[player_action + 1:]
        if is_winning(new_state) == MAX_WIN:
            return MAX_WIN
        self.tree.select_next_root(new_state)
        self.tree.expend(1)
        # TODO: play computer turn
        return self.tree.is_winning()
