class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l +1 : r]
        ans = ''
        for i in range(len(s)):
            t1 = helper(i, i)
            if len(t1) > len(ans):
                ans = t1
            t2 = helper(i, i+1)
            if len(t2) > len(ans):
                ans = t2
        return ans