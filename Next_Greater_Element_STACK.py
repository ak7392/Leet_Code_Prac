# def Nge_Stack(arr: [int]) -> [int]:
# 	mapper = {}
# 	stack = [arr[0]]
# 	nums = set(arr)
# 	for i in range(1, len(arr)):
# 		while stack and arr[i] > stack[-1]:
# 			mapper[stack.pop()] = arr[i]

# 		stack.append(arr[i])

# 	for key in stack: 
# 		mapper[i] = -1 

# 	print([mapper[key] for key in nums])

# a = [1,4,5,6,2,9,1]
# Nge_Stack(a)

def createStack():
	stack = []
	return stack
 
def isEmpty(stack):
	return len(stack) == 0
 
def push(stack, x):
	stack.append(x)
 
def pop(stack):
	if isEmpty(stack):
		print("Error : stack underflow")
	else:
		return stack.pop()
 
'''prints element and NGE pair for all elements of
   arr[] '''
def printNGE(arr):
	s = createStack()
	element = 0
	next = 0
 
    # push the first element to stack
	push(s, arr[0])
 
    # iterate for rest of the elements
	for i in range(1, len(arr), 1):
		next = arr[i]
 
		if isEmpty(s) == False:
 
            # if stack is not empty, then pop an element from stack
			element = pop(s)
 
            # '''If the popped element is smaller than next, then
            #     a) print the pair
            #     b) keep popping while elements are smaller and
            #        stack is not empty '''
			while element < next :
				print(str(element)+ " -- " + str(next))
				if isEmpty(s) == True:
					break
				element = pop(s)
 
            # '''If element is greater than next, then push
            #    the element back '''
			if  element > next:
				push(s, element)
 
        # '''push next to stack so that we can find
        #    next greater for it '''
		push(s, next)
 
    # '''After iterating over the loop, the remaining
    #    elements in stack do not have the next greater
    #    element, so print -1 for them '''
 
	while isEmpty(s) == False:
		element = pop(s)
		next = -1
	print(str(element) + " -- " + str(next))


arr = [3,4,5,9,86,2]
printNGE(arr)