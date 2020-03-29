def subArraySum(arr, n, target):

    temp_sum = {}
    curr_sum = 0

    for i in range(0, n):

        curr_sum += arr[i]

        if curr_sum == target:
            index = i
            print("Sum found between indexes 0 to", index)

        if curr_sum - target in temp_sum:

            print("Subarray exits with given Sum from index :" +
                  str(temp_sum[curr_sum - target]+1) + "to"+str(index))

        temp_sum[curr_sum] = i

    print("No Subarray Sum exists")


arr = [10, 2, -2, -20, 10]
n = len(arr)
target = -10

subArraySum(arr, n, target)
