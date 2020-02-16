def isEmpty(stack): 
	if len(stack) == 0:
		return True
	return False 

def push(stack, ele): 
	stack.append(ele)
	return stack

def pop(stack): 
	if isEmpty == True:
		print("Stack underflow error")
	else:
	
		return stack.pop()

def createStack(): 
	stack = []
	return stack


def NGE_print(arr): 
	s = createStack()
	element = 0
	next = 0

	push(s, arr[0])
	for i in range(1, len(arr), 1): 

		next = arr[i]

		if isEmpty(s) == False: 

			element = pop(s)

			while element < next: 

				print(str(element)+ "---->"+ str(next))
				if isEmpty(s) == True:
					break
				element = pop(s)


			if element > next:
				push(s, element)
		else: 
			push(s, next)

	while isEmpty == False: 
		element = pop(s)
		next = -1
	print(str(element)+ "---->" + str(next))


arr = [1,2,3,4,4,5,5,6,7,8]
NGE_print(arr)

