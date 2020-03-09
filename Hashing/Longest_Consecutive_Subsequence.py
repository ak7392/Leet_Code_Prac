def longest_consecutive_Sub(arr):

    if len(arr) == 0:
        return 0

    dic = {}

    for i in arr:
        dic[i] = True

    for key, value in dic.items():
        if dic.get(key+1) in dic:
            dic[key] = False
            dic[key+1] = False

        else:
            continue

    print(dic)
    max_temp = 1
    for key, value in dic.items():
        temp = 1
        if dic.get(key) == False:
            while (dic.get(key+temp)) == False:
                temp += 1

            if temp > max_temp:
                max_temp = max(temp, max_temp)

    return max_temp


arr = arr = [1, 2, 3, 44, 6, 7]
print(longest_consecutive_Sub(arr))
