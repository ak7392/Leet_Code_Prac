def Longest_consecutive_substring_sets(arr):
    # for each num I will check whether num-1 exists
    # if yes, then I ignore this num
    # Otherwise if num-1 doesn't exist, then I will go till I can find num+1
    # so in a way I am only checking each number max once and once in set.

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
