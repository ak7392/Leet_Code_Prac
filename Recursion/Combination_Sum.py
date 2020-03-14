def combinationSum(candidates, target):
    combination_helper(candidates, [], 0, target)


def combination_helper(candidates, sublist, index, target):
    if target == 0:
        print(sublist)
        return
    if target < 0:
        return
    for i in range(index, len(candidates)):
        sublist.append(candidates[i])
        combination_helper(candidates, sublist, i, target-candidates[i])
        sublist.remove(candidates[i])


arr = [2, 3, 6, 7]
target = 8
combinationSum(arr, target)
