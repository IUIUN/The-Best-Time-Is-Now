class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')' : '(', '}': '{', ']':'['}
        stack = []
        for n in s:
            if n in '( { [':
                stack.append(n)
            elif n in ') } ]':
                if stack == [] or dic[n] != stack.pop():
                    return False
            else:
                return False
        return stack == []
             