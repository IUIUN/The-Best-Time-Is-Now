class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board_next = copy.deepcopy(board)
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                lod = self.liveOrDead(board, i, j)
                if lod == 2:
                    board_next[i][j] = 0
                if lod == 1:
                    board_next[i][j] = 1
        for i in range(m):
            for j in range(n):
                board[i][j] = board_next[i][j]
    def liveOrDead(self, board, i, j):
        ds = [(1,1), (1,-1), (1,0), (-1, 0), (0,1), (0, -1), (-1,-1), (-1,1)]
        count = 0
        m, n = len(board), len(board[0])
        for d in ds:
            r, c = i + d[0], j +d[1]
            if 0 <= r < m and 0 <= c < n:
                if board[r][c] == 1:
                    count += 1
        if count < 2 or count > 3:
            return 2
        elif board[i][j] == 1 or(count == 3 and board[i][j] == 0):
            return 1
        else:
            return 0


        