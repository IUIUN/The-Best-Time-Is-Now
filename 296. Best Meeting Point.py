class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        res = 0
        locs = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    locs.append((i, j))
        locs.sort(key = lambda x:x[0])
        x = locs[len(locs)//2][0]
        for point in locs:
            res += abs(point[0] - x) 
        
        locs.sort(key = lambda x:x[1])
        y = locs[len(locs)//2][1]
        for point in locs:
            res += abs(point[1] - y)
        
        return res
        
//
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        r, c = len(grid), len(grid[0])
        sumr = [i for i in range(r) for j in range(c) if grid[i][j]]
        sumc = [j for i in range(r) for j in range(c) if grid[i][j]]
        sumr.sort()
        sumc.sort()
        mid_row = sumr[len(sumr)//2]
        mid_col = sumc[len(sumc)//2]
        return sum([abs(r-mid_row) for r in sumr]) + sum([abs(c-mid_col) for c in sumc])