def NextGreaterElement(arr: [int]) -> [int]:
	
	n = len(arr)
	i = 0
	j = 0
	for i in range(n): 
		next = -1
		for j in range(i+1, n): 
			if arr[j] > arr[i]:
				next = arr[j]
				break
		print(str(arr[i])+ "---->"+str(next))

	return next

a=[1,2,3,4,5,5,0]
NextGreaterElement(a)