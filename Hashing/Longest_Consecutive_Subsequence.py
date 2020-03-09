def longest_consecutive_Sub(arr):

    if len(arr) == 0:
        return 0

    dic = {}

    for i in arr:
        dic[i] = True

    # Marking all the elemensts in Sequence with Flag False using below Logic
    for key, value in dic.items():
        if dic.get(key+1) in dic:
            dic[key] = False
            dic[key+1] = False

        else:
            continue

    # Using the same dictionary Flag
    print(dic)
    max_temp = 1
    for key, value in dic.items():
        temp = 1
        # Checking where the Flag False is started for giving start of the series
        if dic.get(key) == False:
            # Continue to log the temp count with number of False flag encountered
            while (dic.get(key+temp)) == False:
                temp += 1

            if temp > max_temp:
                max_temp = max(temp, max_temp)

    return max_temp


arr = [1, 2, 3, 4, 5, 6, 7]
print(longest_consecutive_Sub(arr))
