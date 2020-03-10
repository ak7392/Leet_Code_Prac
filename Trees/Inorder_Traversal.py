class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution():
    def inorder_traversal(self, root: TreeNode) -> [int]:

        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left

            if not stack:
                return res

            node = stack.pop()
            res.append(node.val)
            root = node.right


root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(7)
root.right.left = TreeNode(8)
root.right.right = TreeNode(9)
a = Solution()
print(a.inorder_traversal(root))
