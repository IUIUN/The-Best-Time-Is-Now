class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, self.dfs(grid, i, j))
        return maxArea
    def dfs(self, grid, i ,j):
        tmpArea = 0
        if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] != 1:
            return 0
        grid[i][j] = "#"
        left = self.dfs(grid, i - 1, j)
        right = self.dfs(grid, i + 1, j)
        up = self.dfs(grid, i, j - 1)
        down = self.dfs(grid, i, j + 1)
        return left + right + up + down + 1