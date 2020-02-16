class Node:

	def __init__(self, data):
		self.data = data
		self.next = None


class Stack: 

	def __init__(self):
		self.head = None

	def isEmpty(self): 
		if self.head == None: 
			return True
		else: 
			return False 

	def push(self, data): 

		Newnode = Node(data)
		Newnode.next = self.head
		self.head = Newnode


	def pop(self): 

		if self.isEmpty(): 
			return None
		else:

			PopNode = self.head
			self.head = self.head.next
			PopNode.next = None
			print(PopNode.data)

	def peek(self):

		if self.isEmpty(): 
			return None
		else:
			return self.head.data

	def display(self):

		iternode = self.head
		while iternode != None:
			print("--->"+str(iternode.data)+"\n")
			iternode = iternode.next
		return 

My_Stack = Stack()

My_Stack.push(11)
My_Stack.push(13)
My_Stack.push(15)

My_Stack.pop()
print(My_Stack.peek())

# My_Stack.display()





