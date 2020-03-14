def combinationSum(candidates, target):
    combination_helper(candidates, [], 0, target)


def combination_helper(candidates, sublist, index, target):
    if target == 0:
        return sublist
    if target < 0:
        return
    for i in range(index, len(candidates)):
        sublist.append(candidates[i])
        combination_helper(candidates, sublist, i, target-candidates[i])
        sublist.remove(candidates[i])


arr = [10, 1, 2, 7, 6, 1, 5]
target = 7
print(combinationSum(arr, target))
