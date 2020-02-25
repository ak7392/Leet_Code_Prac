INT_MAX = 4294967296
INT_MIN = -4294967296

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.right = None
		self.left = None


class Solution: 
	def __init__(self, x :TreeNode):
		print(self.isValidBinaryTree(x, INT_MIN, INT_MAX))
	# @staticmethod
	def isValidBinaryTree(self, root :TreeNode, mn= INT_MIN, mx= INT_MAX) -> bool :
		# print(root.val, mn, mx)
		if root is None:
			return True
		print(type(root))
		if root.val <= mn or root.val >= mx:
			return False
		if root.left is not None and root.left.val > root.val:
			return False
		if root.right is not None and root.right.val < root.val:
			return False
		return self.isValidBinaryTree(root.left, mn=mn, mx= root.val) and self.isValidBinaryTree(root.right, mn=root.val, mx=mx)


root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)

Solution(root)
# \
# print(a.isValidBinaryTree(root, INT_MIN, INT_MAX))

