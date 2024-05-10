import app.src.datastructure.HexConstants as HexConstants
from app.src.datastructure.tree.Node import Node
from app.src.datastructure.tree.Tree import Tree


def expend_from_node(node, depth, tree):
    res = is_winning(node.state)
    if res != HexConstants.UNFINISHED or depth == 0:
        tree.leafs.append(node)
        node.is_leaf = True
        node.is_ending = res != HexConstants.UNFINISHED
        node.e = 5 if res == HexConstants.MAX_WIN else -5 if res == HexConstants.MIN_WIN else 0
        return node
    successors_states = generate_next_node_state_list(node.state, 'm' if node.is_max else 'M')
    for state in successors_states:
        if len(successors_states) > 0:
            tree.leafs.remove(node)
        child_node = Node(not node.is_max, False, 0, node, state)
        node.successors.append(expend_from_node(child_node, depth - 1, tree))
    return node


def generate_tree(depth):
    if depth == 0:
        return None
    root_state = '_' * HexConstants.CASES_NB
    if depth == 1:
        node = Node(True, True, 0, None, root_state)
        tree = Tree(node)
        tree.leafs.append(node)
        return tree
    node = Node(False, False, 0, None, root_state)
    tree = Tree(node)
    tree.root.successors.append(expend_from_node(node, depth - 1, tree))
    return tree


def generate_next_node_state_list(state, player_char):
    res = []
    for c in HexConstants.CASES:
        if state[c] == HexConstants.NODE_STATE_EMPTY:
            new_state = state[:c] + player_char + state[c + 1:]
            res.append(new_state)
    return res


def is_winning(state):
    def evaluation(list1, list2, stop):
        if not list1:
            return False
        c = list1(0)
        if c in stop:
            return True

        def filter_neighbours(neighbour):
            return neighbour not in list2 and state(c) == state(neighbour)

        neighbours = filter(filter_neighbours, HexConstants.get_neighbours(c))
        list2.append(list1.pop(0))
        return evaluation(list1 + neighbours, list2, stop)

    for case in HexConstants.MAX_START:
        if evaluation([case], [], HexConstants.MAX_STOP):
            return HexConstants.MAX_WIN
    for case in HexConstants.MIN_START:
        if evaluation([case], [], HexConstants.MIN_STOP):
            return HexConstants.MIN_WIN
    return HexConstants.UNFINISHED
