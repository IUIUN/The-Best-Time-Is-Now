class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        if nums[left] ==target:
            return left
        if nums[right] ==target:
            return right
        while left +1 < right:
            mid = left + (right- left)//2
            if target == nums[mid]:
                return mid
            if nums[left] < nums[mid]:
                if nums[left] < target <nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] < target < nums[right]:
                    left = mid
                else:
                    right = mid

        return -1





        
 