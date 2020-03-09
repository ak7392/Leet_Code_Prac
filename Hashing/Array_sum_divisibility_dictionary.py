from collections import defaultdict

"""
def array_sum_divisibility(arr, target):

    dic = defaultdict(lambda: 0)
    result = []
    for i in range(len(arr)):
        num = arr[i] % target
        if dic[arr[i]] == 0:
            dic[arr[i]] = num

    val_sum = 0
    result = list(dic)
    for key in result:

        sum_minus_element = target - dic[key]
        if dic[sum_minus_element] in result:
            result.pop(dic[sum_minus_element])
            result.pop(dic[key])
        else:
            break

    print(result)

    if len(result) == 0:
        return True
    else:
        return False
"""

arr = [2, 2, 1, 3]
target = 4
#print(array_sum_divisibility(arr, target))


def findpairs(a, target):
    d = defaultdict(int)
    for ai in a:
        d[ai % target] += 1
    print(d)
    for di in d:
        if target == di*2:
            if d[di] % 2 != 0:
                return False
        else:
            if d[di] != d[target - di]:
                return False
    return True


print(findpairs(arr, target))
