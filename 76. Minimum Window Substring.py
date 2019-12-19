class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        left, cnt, minLen = 0, 0, float('inf')
        count = collections.Counter(t)
        for i, c in enumerate(s):
            count[c] -= 1
            if count[c] >= 0:
                cnt += 1
            while cnt == len(t):
                if minLen > i - left + 1:
                    minLen = i - left + 1
                    res = s[left : i + 1]
                count[s[left]] += 1
                if count[s[left]] > 0:
                    cnt -= 1
                left +=1
        return res
        
        
