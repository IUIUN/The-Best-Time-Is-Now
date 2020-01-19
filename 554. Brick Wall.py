class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        num = collections.defaultdict(int)
        for i in wall:
            s = 0
            for j in i[:-1]:
                s += j
                num[s] += 1
        return len(wall)-max(num.values(), default = 0)
    
       