//O(mn), the worst
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        temp = [[matrix[i][j] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if not temp[i][j]:
                    self.setZero(i, j, n, m, matrix)
    
    def setZero(self, row, col, n, m, matrix):
        for i in range(m):
            matrix[i][col] = 0
        for j in range(n):
            matrix[row][j] = 0
    
// O(m + n)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row, col = [0 for i in range(m)], [0 for j in range(n)]
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    row[i] = col[j] = 1
        for i in range(m):
            if row[i]:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(n):
            if col[j]:
                for i in range(m):
                    matrix[i][j] = 0
                    
        
                    
            
             
        