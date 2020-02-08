class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        islands_shape = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    positions = []
                    self.dfs(grid, i, j, positions, (0, 0))
                    islands_shape.add(tuple(positions))
        return len(islands_shape)
    def dfs(self, grid, i, j, positions, real_pos):
        grid[i][j] = "#"
        for direction in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            next_i, next_j = i + direction[0], j + direction[1]
            if 0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]) and grid[next_i][next_j] == 1:
                new_real_pos = (real_pos[0] + direction[0], real_pos[1] + direction[1])
                positions.append(new_real_pos)
                self.dfs(grid, next_i, next_j, positions, new_real_pos)