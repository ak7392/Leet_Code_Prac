
class Node:
    def __init__(self, key):
        self.key = key
        self.h_value = 0
        self.depth = 0
        self.right, self.left = None, None


def augment(node, parent, state):
    if node == None:
        return
    if parent == None:
        node.h_value = 0
        node.depth = 0
    else:
        node.depth = parent.depth + 1
        print(node.depth)
        if node == parent.left:
            node.h_value = parent.h_value - 1
        if node == parent.right:
            node.h_value = parent.h_value + 1

    if node.h_value not in state:
        state[node.h_value] = []

    state[node.h_value].append(node.key)

    augment(node.left, node, state)
    augment(node.right, node, state)


def sol(root):
    state = {}
    res = []
    augment(root, None, state)
    for key in state.keys():
        res.append(state[key])
    return res


root = Node(6)
root.left = Node(4)
root.right = Node(7)
root.left.left = Node(3)
root.left.right = Node(5)


print(sol(root))
