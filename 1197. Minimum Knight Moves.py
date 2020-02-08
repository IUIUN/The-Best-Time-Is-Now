class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        cache = {(0, 0): 0, (1, 1): 2, (1, 0): 3, (0, 1): 3}
        def dfs(x, y):
            if (x, y) in cache: return cache[(x, y)]
            res = min(dfs(abs(x-1), abs(y-2)), dfs(abs(x-2), abs(y-1))) + 1
            cache[(x, y)] = res
            return res
        return dfs(abs(x), abs(y))
                    

           

//
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x ==0 and y ==0:
            return 0
        stack = collections.deque([(0,0)])
        cnt = 0
        seen = set()
        seen.add((0,0))
        while stack:
            cnt += 1
            for i in range(len(stack)):
                next_x, next_y = stack.popleft()
                for direction in ((2,1), (-2, 1), (2, -1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)):
                    new_x, new_y = next_x + direction[0], next_y + direction[1]
                    if (new_x, new_y) not in seen:
                        if new_x == x and new_y == y:
                            return cnt
                        seen.add((new_x, new_y))
                        stack.append((new_x, new_y))
        return cnt
                    

           
