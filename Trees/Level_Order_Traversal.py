from Inorder_Traversal import TreeNode
from collections import deque


class Solution:
    def level_Order(self, root):
        levels = []

        if not root:
            return levels

        level = 0
        queue = deque([root, ])

        while queue:
            levels.append([])
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                levels[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1

        return levels


root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(7)
root.right.left = TreeNode(8)
root.right.right = TreeNode(9)
a = Solution()
print(a.level_Order(root))
