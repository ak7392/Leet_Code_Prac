# Method1
# def missing_num(arr):
#     for i in range(len(arr)-1):
#         if arr[i] + 1 != arr[i+1]:
#             print(arr[i+1]-1)
#         else:
#             continue

# Method2


def missing_num(arr):
    n = len(arr)
    total_sum = (n+1) * (n+2) // 2
    temp_sum = sum(arr)
    missing_num = total_sum - temp_sum
    print(missing_num)


arr = [1, 2, 3, 5]
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 10]
missing_num(arr)
missing_num(arr2)
