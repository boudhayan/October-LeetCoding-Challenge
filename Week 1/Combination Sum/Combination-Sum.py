
def combinationSum(candidates, target):
    candidates.sort()
    combinations = []

    def solve(index=0, currentSum=0, taken=list()):
        if currentSum == target:
            combinations.append(taken[:])
            return
        for i in range(index, len(candidates)):
            if currentSum + candidates[index] > target:
                break
            solve(i, currentSum + candidates[i], taken + [candidates[i]])
    solve()
    return combinations


print(combinationSum([3, 4, 5], 8))
