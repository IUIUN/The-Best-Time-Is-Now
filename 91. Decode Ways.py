def numDecodings(s):
    dp = [0]*(len(s)+1)
    dp[0] = 1
    for i in range(1, len(dp)):
        if s[i-1]!= '0':
            dp[i] = dp[i-1]
        if i != 1 and '09' < s[i-2:i] < '27':
            dp[i] += dp[i-2]
    return dp[-1]
if __name__ == "__main__":
    s = "12"
    n = numDecodings(s)
    print(n)