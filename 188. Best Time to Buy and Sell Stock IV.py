class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        if k >= len(prices)//2:
            return self.maxN(prices)
        else:
            return self.maxK(prices, k)
    def maxN(self, prices):
        max_ = 0
        
        for i in range(len(prices) - 1):
            max_ += max(0, prices[i+1] - prices[i])
        return max_
    
    def maxK(self, prices, k):
        maxBuy = [float("-inf") for _ in range(k+1)]
        maxSell = [0 for _ in range(k+1)]
        for i in range(len(prices)):
            for j in range(1, min(k, i//2+1) + 1):
                maxBuy[j] = max(maxBuy[j], maxSell[j-1] - prices[i])
                maxSell[j] = max(maxSell[j], maxBuy[j] + prices[i])
        return maxSell[k]
//method2:
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k <= 0 or not prices: return 0
        N = len(prices)
        if k >= N:
            _sum = 0
            for i in range(1, N):
                if prices[i] > prices[i - 1]:
                    _sum += prices[i] - prices[i - 1]
            return _sum
        g = [0] * (k + 1)
        l = [0] * (k + 1)
        for i in range(N - 1):
            diff = prices[i + 1] - prices[i]
            for j in range(k, 0, -1):
                l[j] = max(g[j - 1] + max(diff, 0), l[j] + diff)
                g[j] = max(l[j], g[j])
        return g[-1]

