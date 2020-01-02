class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for n in range(num+1):
            rst = 0
            while(n):
                n &= n-1
                rst += 1
            # mask = 1
            # for i in range(32):
            #     if n & mask:
            #         rst += 1
            #     mask = mask << 1
            res.append(rst)
        return res


//DP 
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num + 1)
        for i in range(1, num + 1):
            res[i] = res[i // 2] + i % 2
        return res