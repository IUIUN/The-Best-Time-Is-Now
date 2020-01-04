import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        profit = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(len(prices))]
        
        profit[0][0][0], profit[0][0][1] = 0, -prices[0]
        profit[0][1][0], profit[0][1][1] = -sys.maxsize, -sys.maxsize
        profit[0][2][0], profit[0][2][1] = -sys.maxsize, -sys.maxsize
        
        for i in range(1, len(prices)):
            profit[i][0][0] = profit[i-1][0][0]
            profit[i][0][1] = max(profit[i-1][0][1], profit[i-1][0][0] - prices[i])
            
            profit[i][1][0] = max(profit[i-1][1][0], profit[i-1][0][1] + prices[i])
            profit[i][1][1] = max(profit[i-1][1][1], profit[i-1][1][0] - prices[i])
            
            profit[i][2][0] = max(profit[i-1][2][0], profit[i-1][1][1] + prices[i])
            
        end = len(prices) - 1
        return max(profit[end][0][0], profit[end][1][0], profit[end][2][0])

//
        length=len(prices)
        if length==0: return 0
        f1=[0 for i in range(length)]
        f2=[0 for i in range(length)]
        
        minV=prices[0]; f1[0]=0
        for i in range(1,length):
            minV=min(minV, prices[i])
            f1[i]=max(f1[i-1],prices[i]-minV)
            
        maxV=prices[length-1]; f2[length-1]=0
        for i in range(length-2,-1,-1):
            maxV=max(maxV,prices[i])
            f2[i]=max(f2[i+1],maxV-prices[i])
        
        res=0
        for i in range(length):
            if f1[i]+f2[i]>res: res=f1[i]+f2[i]
        return res