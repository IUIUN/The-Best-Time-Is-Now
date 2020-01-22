class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        start, end = 0, 0
        i = 0
        for j, char in enumerate(s, 1):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            if missing == 0:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                need[s[i]] += 1
                missing += 1
                if end == 0 or j - i < end - start:
                    start, end = i, j
                i += 1
        return s[start:end]
       

