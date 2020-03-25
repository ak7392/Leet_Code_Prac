# Minimum Depth of Binary Tree
# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the
# shortest path from the root node down to the nearest leaf
# node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def minDepth(self, root: TreeNode) -> int:

        if root is None:
            return 0

        if root.left == 0 or root.right == 0:
            return 1

        if root.left == None:
            return self.minDepth(root.right)

        elif root.right == None:
            return self.minDepth(root.left)

        else:
            return min(self.minDepth(root.right), self.minDepth(root.left)) + 1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

a = Solution()
print(a.minDepth(root))

