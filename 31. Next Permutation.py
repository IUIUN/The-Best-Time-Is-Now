class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 先找到从后向前数，第一个降序的位置，把此位置后面的翻转。再把这个降序数字和后面第一个比它大的位置交换即可
        n = len(nums)
        i = n - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        self.reverse(nums, i, n - 1)
        if i > 0:
            for j in range(i, n):
                if nums[j] > nums[i-1]:
                    self.swap(nums, i-1, j)
                    break
        
    def reverse(self, nums, i, j):
        """
        contains i and j.
        """
        for k in range(i, (i + j) // 2 + 1):
            self.swap(nums, k, i + j - k)

        
    def swap(self, nums, i, j):
        """
        contains i and j.
        """
        nums[i], nums[j] = nums[j], nums[i]

        
   