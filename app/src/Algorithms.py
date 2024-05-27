from src.datastructure import HexConstants


def minimax(node):
    if node.is_leaf:
        val = node.e
    else:
        if node.is_max:
            val = float('-inf')
            for successor in node.successors:
                val = max(val, minimax(successor))
        else:
            val = float('inf')
            for successor in node.successors:
                val = min(val, minimax(successor))
    return val


def negamax(node):
    if node.is_leaf:
        val = node.e
    else:
        val = float('-inf')
        for successor in node.successors:
            val = max(val, -negamax(successor))
    return val


def alphabeta(node, alpha, beta):
    if node.is_leaf:
        return node.e
    if node.is_max:
        i = 0
        while alpha < beta and i < len(node.successors):
            alpha = max(alpha, alphabeta(node.successors[i], alpha, beta))
            i += 1
        return alpha
    else:
        i = 0
        while alpha < beta and i < len(node.successors):
            beta = min(beta, alphabeta(node.successors[i], alpha, beta))
            i += 1
        return beta


def negalphabeta(node, alpha, beta):
    if node.is_leaf:
        val = node.e
    else:
        val = float('-inf')
        i = 0
        while alpha < beta and i < len(node.successors):
            val = max(val, -negalphabeta(node.successors[i], -beta, -alpha))
            alpha = max(alpha, val)
            i += 1
    return val


def sss(node):
    class PriorityQueue:
        def __init__(self):
            self.queue = []

        def insert(self, n, alive, val):
            self.queue.append([n, alive, val])
            self.queue.sort(reverse=True, key=lambda x: x[2])

        def first(self):
            return self.queue[0]

        def remove_by_successors(self, parent):
            for j in range(len(self.queue)):
                if self.queue[j][0] in parent.successors:
                    self.queue.pop(j)

        def pop(self):
            return self.queue.pop(0)

    discovered_node = [node]
    g = PriorityQueue()
    g.insert(node, True, float('inf'))
    while g.first()[0] != node or not g.first()[1] or g.first()[2] == float('inf'):
        element = g.pop()
        n = element[0]
        e = element[2]
        if n not in discovered_node:
            discovered_node.append(n)
        if element[1]:
            if n.is_leaf:
                g.insert(n, False, min(e, n.e))
            else:
                if n.is_max:
                    for i in range(0, len(n.successors)):
                        g.insert(n.successors[i], True, e)
                else:
                    for successor in n.successors:
                        if successor not in discovered_node:
                            g.insert(successor, True, e)
                            break
        else:
            if n.is_max:
                siblings = n.pred.successors
                index = siblings.index(n)
                next_sibling = siblings[index + 1]
                if next_sibling is not None:
                    g.insert(next_sibling, True, e)
                else:
                    g.insert(n.pred, False, e)
            else:
                g.insert(n.pred, False, e)
                g.remove_by_successors(n.pred)
    return g.pop()[2]


def AStar(state, start_case, end_cases):
    #TODO
    return 1.0


def heuristic(node):
    def is_connected_to_side(list1, list2, start_side, end_side):
        if not list1:
            return '_'
        c = list1(0)
        if c in start_side:
            return 's'
        if c in end_side:
            return 'e'

        def filter_neighbours(neighbour):
            return neighbour not in list2 and node.state(c) == node.state(neighbour)

        neighbours = filter(filter_neighbours, HexConstants.get_neighbours(c))
        list2.append(list1.pop(0))
        return is_connected_to_side(list1 + neighbours, list2, start_side, end_side)

    if node.is_ending:
        return 1.5 if node.is_max else -1.5
    plus = 0
    minus = 0
    for i in range(HexConstants.CASES_NB):
        if node.state[i] == HexConstants.NODE_STATE_MAX:
            side = is_connected_to_side([i], [], HexConstants.MAX_START, HexConstants.MAX_STOP)
            if side == 's':
                dist = AStar(node.state, i, HexConstants.MAX_STOP)
                plus = max(plus, 1 / dist)
            elif side == 'e':
                dist = AStar(node.state, i, HexConstants.MAX_START)
                plus = max(plus, 1 / dist)
        if node.state[i] == HexConstants.NODE_STATE_MIN:
            side = is_connected_to_side([i], [], HexConstants.MIN_START, HexConstants.MIN_STOP)
            if side == 's':
                dist = AStar(node.state, i, HexConstants.MIN_STOP)
                minus = min(minus, 1 / dist)
            elif side == 'e':
                dist = AStar(node.state, i, HexConstants.MIN_START)
                minus = min(minus, 1 / dist)
    return plus - minus
