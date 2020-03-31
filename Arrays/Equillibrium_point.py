def equillibrium(arr):

    low = 0
    high = len(arr)-1
    curr_sum1 = 0
    curr_sum2 = 0

    # For more optimized solution refer below link:
    # https://www.geeksforgeeks.org/equilibrium-index-of-an-array/
    while low <= high:

        if curr_sum1 <= (curr_sum2 + arr[high]):
            curr_sum1 += arr[low]
            low += 1
            if curr_sum1 == curr_sum2:
                print(arr[low])
        while curr_sum2 <= curr_sum1:
            curr_sum2 += arr[high]
            high -= 1
            if curr_sum1 == curr_sum2:
                print(arr[high])


arr = [4, 5, 8, 3, 17]
arr2 = [4, 5, 8, 3, 6]
equillibrium(arr)
equillibrium(arr2)
