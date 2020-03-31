def reverse_array_groups(arr, n):
    low = 0
    high = len(arr)-1
    stack = []
    new_stack = []

    while low < high:

        stack.append(arr[low])
        low += 1

        if low == n-1:
            for i in stack:
                new_stack.append(stack.pop(i))

    print(new_stack)


arr = [10, 20, 30, 40, 50, 60]
n = 3
reverse_array_groups(arr, n)
