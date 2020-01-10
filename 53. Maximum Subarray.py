class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return None
        dp = [ _ for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = nums[i] + (dp[i-1] if dp[i-1] > 0 else 0)
        return max(dp)
    
#         if max(nums)<0:
#             return max(nums)
        
#         local_max, global_max = 0, 0
#         for num in nums:
#             local_max = max(0, local_max + num)
#             global_max = max(global_max, local_max)
            
#         return global_max