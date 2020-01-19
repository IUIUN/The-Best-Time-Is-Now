class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = collections.defaultdict(int)
        dic[0] = 1
        sum = 0
        res = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in dic:
                res += dic[sum - k]
            dic[sum] += 1
        return res
                
        