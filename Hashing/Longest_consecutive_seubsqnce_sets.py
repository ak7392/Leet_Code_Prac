def Longest_consecutive_substring_sets(arr):

    nums = set(arr)
    mx = 0
    for num in nums:
        if num-1 not in nums:
            temp = 1
            while num+1 in nums:
                temp += 1
                num += 1

            mx = max(mx, temp)

    return mx


arr = [1, 2, 3, 44, 6, 7]
print(Longest_consecutive_substring_sets(arr))
