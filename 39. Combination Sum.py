1. Recursion(DFS)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, 0, [], target, res)
        return res
    def dfs(self, candidates, index, path, target, res):
        if target == 0:
            res.append(path)
        else:
            for i in range(index, len(candidates)):
                if candidates[i] > target:
                    break
                else:
                    self.dfs(candidates, i, path + [candidates[i]], target - candidates[i], res)

2. backtracking
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.backtracking(sorted(candidates), target, [], 0, res)
        return res
    def backtracking(self, nums, target, intermediate, start, res):
        if target == 0:
            res.append(list(intermediate))
        while start < len(nums) and nums[start] <= target:
            intermediate.append(nums[start])
            self.backtracking(nums, target - nums[start], intermediate, start, res)
            intermediate.pop()
            start += 1