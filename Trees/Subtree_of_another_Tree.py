from Inorder_Traversal import TreeNode


class Solution:
    def equals(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return False
        if not s or not t:
            return False
        return s.val == t.val and self.equals(s.right, t.right) and self.equals(s.left, t.left)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False

        if self.equals(s, t) or self.isSubtree(s.right, t) or self.isSubtree(s.left, t):
            return True


s = TreeNode(3)
s.left = TreeNode(4)

t = TreeNode(6)
t.left = TreeNode(7)
t.right = TreeNode(8)

s.right = t
a = Solution()
a.isSubtree(s, t)
