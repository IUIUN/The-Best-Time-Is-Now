class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for _ in range(amount+1)]
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i-coin]+1, dp[i])
        return -1 if dp[amount] > amount else dp[amount]
    
                
                
                
        
    