class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        sum_so_far = 0
        for i in range(len(nums)):
            if sum_so_far*2 + nums[i] == total_sum:
                return i
            else:
                sum_so_far += nums[i]
        return -1