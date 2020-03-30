def rearrange_array(arr, n):
    # Initialize index of first minimum
    # and first maximum element
    max_idx = n - 1
    min_idx = 0

    # Store maximum element of array
    # Note if we conside the max element non + 1 then greatest element divide by same gives remainde 0
    # and printing 0 as a remainder and adds to number 1.
    # To make it non zero we have considered + 1 max_element here
    max_elem = arr[n-1] + 1

    # Traverse array elements
    for i in range(0, n):

        # At even index : we have to put maximum element
        if i % 2 == 0:
            print((arr[max_idx] % max_elem) * max_elem)
            arr[i] += (arr[max_idx] % max_elem) * max_elem
            # print(arr[i])
            # print(max_idx)
            max_idx -= 1

        # At odd index : we have to put minimum element
        else:
            arr[i] += (arr[min_idx] % max_elem) * max_elem
            min_idx += 1

    # array elements back to it's original form
    for i in range(0, n):
        arr[i] = arr[i] // max_elem

    return arr


arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
print(rearrange_array(arr, n))
