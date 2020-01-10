class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        start, maxLenth = 0, 0
        for i in range(len(s)):
            if s[i] in dic and start <= dic[s[i]]:
                start = dic[s[i]] + 1
            else:
                maxLenth = max(maxLenth, i - start + 1)
            dic[s[i]] = i
        return maxLenth