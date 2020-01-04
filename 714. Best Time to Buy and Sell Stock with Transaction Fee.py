class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) < 2:
            return 0
        sell = 0
        buy = -prices[0]
        for i in range(1, len(prices)):
            sell = max(sell, buy + prices[i] - fee)
            buy = max(buy, sell - prices[i])
        return sell
    