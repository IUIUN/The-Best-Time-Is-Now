class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0:
            return
        self.solve(board)
        
    def solve(self, board):
        """
        rtype: boolean
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for c in "123456789":
                        if self.isValid(board, i, j, c):
                            board[i][j] = c
                            # If it's the solution return true
                            if self.solve(board): 
                                return True
                            # Otherwise go back
                            else:
                                board[i][j] = '.'
                    return False
        return True
        
    def isValid(self, board, x, y, c):
        for i in range(9):
            if board[i][y] == c: 
                return False
        for j in range(9):
            if board[x][j] == c:
                return False
        for i in range(3):
            for j in range(3):
                if board[(x//3)*3 + i][(y//3)*3 + j] == c:
                    return False
                    
        return True