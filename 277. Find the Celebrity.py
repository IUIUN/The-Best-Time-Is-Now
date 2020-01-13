# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        x = 0
        for i in range(n):
            if knows(x, i):
                x = i
        if any(knows(x, i) for i in range(x)):
            return -1
        if any(not knows(i, x) for i in range(n)):
            return -1
        return x
    