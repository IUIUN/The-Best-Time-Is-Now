class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        for c in "1?'!,;.":
            paragraph = paragraph.replace(c, "")
        d = {}
        cnt = 0
        res = ""
        
        for word in paragraph.lower().split( ):
            if word in banned:
                continue
            elif word in d:
                d[word] += 1
            elif word not in d:
                d[word] = 1
            if d[word] > cnt:
                cnt = d[word]
                res = word
        return res