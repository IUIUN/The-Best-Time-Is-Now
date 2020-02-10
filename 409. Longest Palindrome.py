class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash = set()
        for c in s:
            if c not in hash:
                hash.add(c)
            else:
                hash.remove(c)
        return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)
                
                
            