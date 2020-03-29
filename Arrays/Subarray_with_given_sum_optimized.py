
def sub_sum(array, target):

    temp_sum = 0

    i = 0
    n = 2
    for i in range(n):
        temp_sum += array[i]

    p1 = 0
    p2 = 2
    new_sum = temp_sum
    result = []

    while p1 < len(array):

        new_sum = new_sum - array[p1] + array[p2]

        if new_sum == target:
            result.append(array[p1:p2+1])
        elif array[p2] == target:
            result.append(array[p2])

        p1 += 1
        p2 += 1
    print(result)


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sub_sum(array, 7)
