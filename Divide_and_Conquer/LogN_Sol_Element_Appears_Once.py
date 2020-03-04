def binary_search_unique_ele(arr, low, high):

    # for explanation refer https://www.youtube.com/watch?v=SmdzCnDD_HM

    if low > high:
        return None

    if (low == high):
        return arr[low]
    mid = low + (high - low)//2

    if mid % 2 == 0:

        if arr[mid] == arr[mid+1]:
            return binary_search_unique_ele(arr, mid+2, high)
        else:
            return binary_search_unique_ele(arr, low, mid)

    else:
        # if mid is odd
        if arr[mid] == arr[mid-1]:
            return binary_search_unique_ele(arr, mid+1, high)
        else:
            return binary_search_unique_ele(arr, low, mid-1)


arr = [1, 1, 2, 2, 3, 3, 4, 5, 5]
print(binary_search_unique_ele(arr, 0, len(arr)-1))
