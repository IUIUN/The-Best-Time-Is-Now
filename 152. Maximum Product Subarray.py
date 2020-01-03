class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        curMax, curMin, res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            curMin, curMax = min(curMax * nums[i], curMin* nums[i], nums[i]), max(curMax* nums[i], curMin* nums[i], nums[i])
            res = max(curMax, res)
        return res
//用两个变量代替二维数组，注意curMin, curMax这里的赋值要同时进行不能分开，否则有一个的值会变化，导致错误

//原始解法用DP二维数组，并且使用数组状态压缩节省空间

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [[0 for _ in range(2)] for _ in range(2)]
        dp[0][1], dp[0][0], res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            x, y = i%2, (i-1)%2
            dp[x][0] = max(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            dp[x][1] = min(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            res = max(dp[x][0], res)
        return res
