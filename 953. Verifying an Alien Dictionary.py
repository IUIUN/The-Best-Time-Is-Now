class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        N = len(words)
        d = {c:i for i, c in enumerate(order)}
        for i in range(N-1):
            pre, after = words[i], words[i + 1]
            if pre == after:
                continue
            len_ = min(len(pre), len(after))
            for j in range(len_):
                if d[pre[j]] < d[after[j]]:
                    break
                elif d[pre[j]] > d[after[j]]:
                    return False
            if len(pre) > len(after) and pre[:len_] == after:
                return False
        return True
   