class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None 
		self.right = None 

class Solution: 
	# def __init__(self, p :TreeNode, q :TreeNode):
	# 	print(self.SameTrees(p, q))
	@staticmethod
	def SameTrees(p: TreeNode, q: TreeNode) -> bool : 
		if p is  None and q is  None:
			return True 
		if (p is not None and q is None) or (q is None and p is not None): 
			return False
		while p: 
			 if p.val != q.val:
			 	return False 

			 return Solution.SameTrees(p.left, q.left) and Solution.SameTrees(p.right, q.right)

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

a = Solution()

print(a.SameTrees(p, q))