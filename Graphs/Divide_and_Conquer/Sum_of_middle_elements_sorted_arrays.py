def sum_middle_elements_merged(arr1, arr2):

    new_arr = arr1 + arr2

    # length of new array
    length = len(new_arr)

    low = 0
    high = length - 1

    while(low < high):
        sum = 0
        mid = (low + (high-low))//2

        if mid % 2 == 0:
            sum = new_arr[mid] + new_arr[mid+1]
            return sum
        else:
            sum = new_arr[mid] + new_arr[mid+1]
            return sum


arr1 = [1, 2, 3, 4]
arr2 = [4, 5, 6, 7]
print(sum_middle_elements_merged(arr1, arr2))
