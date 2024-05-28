from src.GameState import GameState
import src.datastructure.TreeManager as TreeManager
from src.datastructure.tree.Node import Node


class Tree:
    def __init__(self, root):
        self.root = root
        self.leafs = []

    def expend(self):
        def aux(nodes):
            if not nodes:
                return
            node = nodes.pop(0)
            if node.is_leaf and not node.is_ending:
                node.is_leaf = False
                successors_states = TreeManager.generate_next_node_state_list(node.state, 'm' if node.is_max else 'M')
                for state in successors_states:
                    child_node = Node(not node.is_max, True, 0, node, state)
                    child_node.is_ending = TreeManager.is_winning(child_node.state) != GameState.UNFINISHED
                    node.successors.append(child_node)
                return aux(nodes)
            return aux(nodes + node.successors)
        return aux([self.root])

    def is_winning(self):
        return TreeManager.is_winning(self.root.state)

    def select_next_root(self, state):
        possible_new_root = self.root.successors
        for node in possible_new_root:
            if node.state == state:
                self.root = node
                return
        raise Exception("Error - unknown state")
