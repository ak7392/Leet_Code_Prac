class Node:
    def __init__(self, value):
        self.val = value
        self.right = None
        self.left = None


class Solution:

    def is_Binary_Tree_satisfied(self, root):
        if root is not None:
            is_balanced = self.is_helper(root, root.val)

            if is_balanced is None:
                return True
            return False

        return True

    def is_helper(self, node, data):
        if node.left:
            if data < node.left.val:
                return self.is_helper(node.left, node.left.data)
            else:
                return False
        if node.right:
            if data > node.right.val:
                return self.is_helper(node.right, node.right.data)
            else:
                return False


root = Node(6)
root.left = Node(4)
root.left.left = Node(3)
root.left.right = Node(5)
root.right = Node(7)
a = Solution()
print(a.is_Binary_Tree_satisfied(root))
