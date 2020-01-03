class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit, minPrice = 0, float("inf")
        for i in prices:
            minPrice = min(i, minPrice)
            maxProfit = max(maxProfit, i - minPrice)
        return maxProfit
    
            
                
        
        