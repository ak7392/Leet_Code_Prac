def Kadane_algorithm(array):
    current_sum = global_sum = array[0]

    for i in range(1, len(array)):
        current_sum = max(array[i], current_sum + array[i])

        if current_sum > global_sum:
            global_sum = current_sum

    return global_sum


array = [1, 2, -3, 4, 5]
print(Kadane_algorithm(array))
