class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=1:
            return n
        res = [0 for i in range(n)]
        res[0] = 1
        res[1] = 2
        for i in range(2, n):
            res[i] = res[i-1] + res[i-2]
        return res[-1]
    //注意res[0] = 1 res[1] = 2


class Solution:
    def climbStairs(self, n: int) -> int:
        x, y = 1, 1
        for _ in range(1, n):
            x, y = y, x + y
        return y