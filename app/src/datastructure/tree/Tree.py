from src.GameState import GameState
import src.datastructure.TreeManager as TreeManager
from src.datastructure.tree.Node import Node


class Tree:
    def __init__(self, root):
        self.root = root
        self.leafs = []

    def expend(self, depth):
        if depth == 0:
            return
        for node in self.leafs:
            res = TreeManager.is_winning(node.state)
            if res == GameState.UNFINISHED:
                node.is_leaf = False
                successors_states = TreeManager.generate_next_node_state_list(node.state, 'm' if node.is_max else 'M')
                for state in successors_states:
                    child_node = Node(not node.is_max, False, 0, node, state)
                    node.successors.append(TreeManager.expend_from_node(child_node, depth - 1, self))

    def is_winning(self):
        return TreeManager.is_winning(self.root.state)

    def select_next_root(self, state):
        possible_new_root = self.root.successors
        for node in possible_new_root:
            if node.state == state:
                self.root = node
                return
        raise Exception("Error - unknown state")
