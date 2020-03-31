# reference of this problem
# https://www.youtube.com/watch?v=ELkxYyd8gxE


def sortnumbers(a):

    low = 0
    high = len(a)-1
    mid = 0
    while mid <= high:

        # mid = (low+high)//2  # You don't need to find the mid this algorithm is tweked binary search

        if a[mid] == 0:
            a[low], a[mid] = a[mid], a[low]
            low += 1
            mid += 1

        if a[mid] == 1:
            mid += 1

        else:
            a[mid], a[high] = a[high], a[mid]
            high -= 1

    return a


#      mid  Both pointers will be at start for this algorithm
#      low                              end
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

#       low  Both pointers will be at start for this algorithm
#                      mid              end   #if mid is at element 2 swap it with end
# arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

#                 low
#                    mid                            end   #if mid is at element 1 swap it with low pointer to sort and move
#           arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

sortnumbers(arr)
print(arr)
