mn = float("-inf")
mx = float("inf")

# Thumb rule for checking BST's is to check whether inorder traversal is satisfied
# from leftmost leaf via root to righmost leaf


class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def isBST(node):
    return isBSTUtil(node, mn, mx)


def isBSTUtil(node, mini, maxi):

    if node is None:
        return True

    elif node.val < mini or node.val > maxi:
        return False

    else:
        return isBSTUtil(node.left, mini, node.val - 1) and isBSTUtil(node.right, node.val+1, maxi)


root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

if isBST(root):
    print("Tree is BST")

else:
    print("Tree is not a BST")
