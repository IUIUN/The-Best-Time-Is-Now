class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        from math import ceil
        L, R = 1, max(nums) + 1
        def check(m):
            s = 0
            for x in nums:
                s += ceil(x/m)
            return s <= threshold
        
        while L < R:
            m = (L + R) // 2
            if check(m):
                ans = m
                R = m
            else:
                L = m + 1
        
        return ans