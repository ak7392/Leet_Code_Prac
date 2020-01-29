class Node:
	def __init__(self, value):
		self.val = value
		self.left = None
		self.right = None

class Solution:
	@staticmethod
	def zigzagLevelOrder(root_List: Node) -> [[int]]:
		res = []
		node = [[root_List]]
		level_count = 0

		while node:
			layer = node.pop()

			if not layer:
				break

			row_val = []
			row_node = []

			level_count += 1

			while layer:
				element = layer.pop()

				if not element:
					continue
				[l,r] = [element.left, element.right]

				if level_count % 2 == 1:
					[l, r] = [r, l]

				row_val.append(element.val)
				row_node.extend([l,r])
			node.append(row_node)
			if row_val:
				res.append(row_val)
		return res



root1 = Node(1)
root2 = Node(2)
root4 = Node(3)
root5 = Node(None)
root6 = Node(None)
root7 = Node(4)
root8 = Node(5)

root1.left = root2
root1.right = root4
root2.left = root5
root2.right = root6
root4.left = root7
root4.right = root8

# root_List = [root1, root2, root4, root5, root6, root7, root8]

a = Solution()

print(a.zigzagLevelOrder(root1))


