from collections import defaultdict


class Node:
    def __init__(self, key):
        self.val = key

        self.right, self.left = None, None


def verticalTraversal(root: Node) -> [[int]]:
    V = []

    def helper(n, x, y):
        if n:
            V.append((x, y, n.val))
            helper(n.left, x-1, y+1)
            helper(n.right, x+1, y+1)

    helper(root, 0, 0)
    V.sort()
    print(V)
    d = defaultdict(list)
    for i, j, k in V:
        d[i].append(k)
    return list(d.values())


root = Node(6)
root.left = Node(4)
root.right = Node(7)
root.left.left = Node(3)
root.left.right = Node(5)


print(verticalTraversal(root))
