class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        else:
            total = 0
            for i in range(1, len(prices)):
                if(prices[i] - prices[i-1] > 0):
                    total += prices[i] - prices[i-1]
            return total
                
        
        
        