class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = right = 0
        counts = collections.defaultdict(int)
        while right < len(s):
            counts[s[right]] += 1
            right += 1
            if len(counts) > 2:
                counts[s[left]] -= 1
                if not counts[s[left]]:
                    del counts[s[left]]
                left += 1
        return right - left
            