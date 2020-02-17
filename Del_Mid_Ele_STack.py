class Stack: 
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def pop(self):
		return self.items.pop()

	def push(self, item): 
		return self.items.append(item)

	def peek(self): 
		return self.items[len(self.items)-1]

	def size(self): 
		return len(self.items)

def del_Middle_ele(st, sizeofstack, current):

	if current == sizeofstack and st.isEmpty():
		return

	x = st.peek()
	st.pop()

	del_Middle_ele(st, sizeofstack, current + 1)

	if current != sizeofstack//2:
		st.push(x)

st = Stack()

st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)
st.push(6)
st.push(7)

del_Middle_ele(st, st.size(), 0)

while st.isEmpty() == False:
	x = st.peek()
	st.pop()
	print(x)
