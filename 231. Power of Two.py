class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n != 0 and n&(n-1) == 0:
            return True
        else:
            return False
        
        # if n <= 0:
        #     return False
        # if n == 1:
        #     return True
        # while n > 1:
        #     if n%2 != 0:
        #         return False
        #     n /= 2
        # return True