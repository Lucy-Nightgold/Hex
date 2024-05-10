from app.src.datastructure import TreeManager
from app.src.datastructure.HexConstants import UNFINISHED
from app.src.datastructure.TreeManager import is_winning, generate_next_node_state_list, expend_from_node
from app.src.datastructure.tree.Node import Node


class Tree:
    def __init__(self, root):
        self.root = root
        self.leafs = []

    def expend(self, depth):
        if depth == 0:
            return
        for node in self.leafs:
            res = is_winning(node.state)
            if res == UNFINISHED:
                node.is_leaf = False
                successors_states = generate_next_node_state_list(node.state, 'm' if node.is_max else 'M')
                for state in successors_states:
                    child_node = Node(not node.is_max, False, 0, node, state)
                    node.successors.append(expend_from_node(child_node, depth - 1, self))

    def is_winning(self):
        return TreeManager.is_winning(self.root.state)

    def select_next_root(self, state):
        possible_new_root = self.root.successors
        for node in possible_new_root:
            if node.state == state:
                self.root = node
                return
        raise Exception("Error - unknown state")
