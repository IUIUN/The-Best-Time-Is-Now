class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res
    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)): 
            self.dfs(nums,i + 1, path + [nums[i]], res )
            print(res)
             
        
       //
    
    def subsets(self, nums):
        
        nums.sort()
        output = [[]]
        
        for num in nums:
            output.extend([subset + [num] for subset in output])
            
        return output