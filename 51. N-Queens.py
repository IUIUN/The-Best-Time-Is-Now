class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.dfs([-1]*n, 0, [], res)
        return res
    def dfs(self, nums, index, path, res):
        if index == len(nums):
            res.append(path)
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.check(nums, index):
                temp = "." * len(nums)
                self.dfs(nums, index + 1, path + [temp[:i] + "Q" + temp[i+1:]], res)
             
    def check(self, nums, index):
        for i in range(index):
            if nums[i] == nums[index] or abs(nums[i] - nums[index]) == abs(i - index):
                return False
        return True


