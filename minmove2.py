from collections import deque

class Move:
    def __init__(self, x, y, step):
        self.x = x
        self.y = y
        self.step = step

def isInside(x, y, n):
    return x >= 0 and x < n and y >= 0 and y < n

def nextMoves(x, y, n):
    AVAILABLE_SHIFTS = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    result = list()
    for shift in AVAILABLE_SHIFTS:
        move_x, move_y = x + shift[0], y + shift[1]
        if isInside(move_x, move_y, n):
            result.append((move_x, move_y))
    return result

def minMoves(n, startX, startY, endX, endY):
    # Write your code here
    queue = deque()
    queue.append(Move(startX, startY, 0))

    visited = dict()
    visited[startX, startY] = True

    while queue:
        t = queue[0]
        queue.popleft()

        if t.x == endX and t.y == endY:
            return t.step

        for move in nextMoves(t.x, t.y, n):
            if move not in visited:
                visited[move] = True
                queue.append(Move(move[0], move[1], t.step + 1))

print(minMoves(7, 6, 6, 0, 1))