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
        self.backtracking(candidates, target, intermediate, start)
        return res
    def backtracking(self, nums, target, intermediate, start):
        if target == 0:
            res.append(intermediate)
        while start <= len(nums) and nums[start] <= target:
            intermediate.append(nums[start])
            self.backtracking(nums, target - nums[start], intermediate, start)
            intermediate.pop()
            start += 1