class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[0 for _ in range(n)] for _ in range(m)]
        cnts = [[0 for _ in range(n)] for _ in range(m)]
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt += 1
                    self.bfs(grid, i, j, dist, cnts)
        min_ = float('inf')
        for i in range(m):
            for j in range(n):
                if dist[i][j] < min_ and cnts[i][j] == cnt:
                    min_ = dist[i][j]
        return min_ if min_ != float('inf') else -1
    
    def bfs(self, grid, i, j, dist, cnts):
        d, m, n = 0, len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        current_layer = [(i, j)]
        while current_layer:
            d += 1
            next_layer = []
            for x, y in current_layer:
                for dir in[(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    X, Y = x + dir[0], y + dir[1]
                    if 0 <= X < m and 0 <= Y < n and grid[X][Y] == 0 and not visited[X][Y]:
                        visited[X][Y] = True
                        dist[X][Y] += d
                        cnts[X][Y] += 1
                        next_layer.append((X, Y))
            current_layer = next_layer
