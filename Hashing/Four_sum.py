def four_sum(arr, target):

    arr = sorted(arr)
    n = len(arr)

    for i in range(n-3):
        for j in range(i+1, n-3):

            l = j+1
            r = n-2

            while(l < r):

                if arr[i] + arr[j] + arr[l] + arr[r] == target:
                    print("The numbers adding up to target element ---> ",
                          arr[i], arr[j], arr[l], arr[r])

                    l += 1
                    r -= 1

                elif arr[i] + arr[j] + arr[l] + arr[r] < target:
                    l += 1
                else:
                    r -= 1


arr = [1, 4, 7, 10, 12, 14, 23, 2]
target = 20
four_sum(arr, target)
