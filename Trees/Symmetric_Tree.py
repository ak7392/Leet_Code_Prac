from Inorder_Traversal import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if root is None:
            return True

        else:
            return self.checkSymmetric(root.left, root.right)

    def checkSymmetric(self, left, right) -> bool:
        if left is None and right is None:
            return True
        if left is not None and right is not None:

            return left.val == right.val and self.checkSymmetric(left.left, right.right) and self.checkSymmetric(left.right, right.left)


root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(7)
root.right.left = TreeNode(8)
root.right.right = TreeNode(9)
a = Solution()
print(a.isSymmetric(root))
