class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = collections.Counter(s)
        chance = 1
        for c in count:
            if count[c] % 2 != 0:
                chance -= 1
            if chance < 0:
                return False
        return True
            