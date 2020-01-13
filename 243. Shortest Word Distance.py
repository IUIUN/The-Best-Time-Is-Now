class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        i,index1, index2 = 0, None, None
        res = float('inf')
        while i < len(words):
            if words[i] == word1:
                index1 = i
            elif words[i] == word2:
                index2 = i
            if index1 is not None and index2 is not None:
                res = min(res, abs(index2 - index1))
            i += 1
        return res
    
    
                
        