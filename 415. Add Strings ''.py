class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res, i, j, s = [], len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0 or s:
            if i >= 0:
                s += int(num1[i])
                i -= 1
            if j >= 0:
                s += int(num2[j])
                j -= 1
            res.append(str(s % 10))
            s //= 10
        return "".join(res[::-1])
            
        
    
            
        
       