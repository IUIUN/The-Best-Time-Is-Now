class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))
        pos = len(res) - 1
        for n1 in reversed(num1):
            tmp_pos = pos
            for n2 in reversed(num2):
                res[tmp_pos] += int(n1) * int(n2)
                res[tmp_pos - 1] += res[tmp_pos] // 10
                res[tmp_pos] %= 10
                tmp_pos -= 1
            pos -= 1
        st = 0
        while st < len(res) - 1 and res[st] == 0:
            st += 1
        return "".join(map(str, res[st:]))
                
                
        
   
                
            
