class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = len)
        dp = collections.defaultdict(int)
        for word in words:
            for i in range(len(word)):
                dp[word] = max(dp[word], dp[word[:i] + word[i+1:]] + 1 )
        return max(dp.values())
        