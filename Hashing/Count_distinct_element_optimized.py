def count_elem_optimized(arr, n, k):
    for i in range(n-k+1):
        s = set(arr[i:i+k])
        return (len(s))


arr = [1, 2, 1, 3, 4, 2, 3]
print(count_elem_optimized(arr, len(arr), 3))
