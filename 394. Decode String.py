class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curNum = 0
        curStr = ''
        for c in s:
            if c == "]":
                num = stack.pop()
                preStr = stack.pop()
                curStr = preStr + num * curStr
            elif c == "[":
                stack.append(curStr)
                stack.append(curNum)
                
                curStr = ''
                curNum = 0
                
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curStr += c
        return curStr
   