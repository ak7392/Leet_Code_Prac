
def sub_sum(array, target):

    temp_sum = 0

    i = 0
    n = 2
    for i in range(n):
        temp_sum += array[i]

    p1 = 0
    p2 = n
    new_sum = temp_sum
    result = []

    while p2 < len(array):

        # we are moving the window while subtracting p1 pointer and keep adding p2 pointer and hence sliding the
        # window forward until p2 pointer is reached.
        temp_sum += array[p2] - array[p1]

        if temp_sum >= new_sum:
            new_sum = temp_sum
            p2 += 1
        else:
            p1 += 1

        p1 += 1
        p2 += 1
    print(new_sum)


array = [1, 1, 4]
sub_sum(array, 7)
