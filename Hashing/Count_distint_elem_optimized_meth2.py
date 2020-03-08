from collections import defaultdict


def Count_distinct_element(arr, k, n):

    #dic = defaultdict(lambda: 0)
    dic_count = 0

    for i in range(k):

        if dic[arr[i]] == 0:
            dic_count += 1
        dic[arr[i]] += 1

    print(dic_count)

    for i in range(k, n):

        if dic[arr[i-k]] == 1:
            dic_count -= 1
        dic[arr[i-k]] -= 1

        if dic[arr[i]] == 0:
            dic_count += 1
        dic[arr[i]] += 1

        print(dic_count)


arr = [1, 2, 1, 3, 4, 2, 3]
n = len(arr)
k = 4
Count_distinct_element(arr, k, n)
