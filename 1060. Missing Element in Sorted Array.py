class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        if not nums or k == 0:
            return 0
        diff = nums[-1] - nums[0] + 1 # complete length
        missing = diff - len(nums) # complete length - real length
        if k > missing: # if k is larger than the number of mssing words in sequence
            return nums[-1] + k - missing
        
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            missing = nums[mid] - nums[left] - (mid - left)
            if missing < k:
                left = mid
                k -= missing # KEY: move left forward, we need to minus the missing words of this range
            else:
                right = mid
                
        return nums[left] + k # k should be between left and right index in the end