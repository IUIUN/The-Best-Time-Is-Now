class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[False for i in range(9)] for i in range(9)]
        col = [[False for i in range(9)] for i in range(9)]
        block = [[False for i in range(9)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    k = i // 3 * 3 + j // 3
                    if row[i][num] or col[j][num] or block[k][num]:
                        return False
                    row[i][num] = col[j][num] = block[k][num] = True
        return True

