class cell:

    def __init__(self, x = 0, y = 0, dist = 0):
        self.x = x
        self.y = y
        self.dist = dist

def isInside(x, y, N):
    if(x >= 0 and x < N and y >= 0 and y < N):
        return True
    return False

def minMoves(n, startX, startY, endX, endY):
    # Write your code here
    dx = [2,2,-2,-2,1,1,-1,-1]
    dy = [1,-1,1,-1,2,-2,2,-2]

    queue = []

    queue.append(cell(startX, startY, 0))

    visited = [[False for i in range(n)] for j in range(n)]

    visited[startX][startY] = True

    while (len(queue) > 0):
        t = queue[0]
        queue.pop(0)

        if (t.x == endX and t.y == endY):
            return t.dist

        for i in range(8):
            x = t.x + dx[i]
            y = t.y + dy[i]

            if (isInside(x, y, n) and not visited[x][y]):
                visited[x][y] = True
                queue.append(cell(x, y, t.dist + 1))

print(minMoves(7, 6, 6, 0, 1))