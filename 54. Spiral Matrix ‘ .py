class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        res = []
        l, r, u, d = 0, n - 1, 0, m - 1
        while l < r and u < d:
            res.extend([matrix[u][j] for j in range(l,r)])
            res.extend([matrix[i][r] for i in range(u,d)])
            res.extend([matrix[d][j] for j in range(r,l,-1)])
            res.extend([matrix[i][l] for i in range(d, u, -1)])
            l, r, u, d = l + 1, r - 1, u + 1, d - 1
        if l == r:
            res.extend([matrix[i][r] for i in range(u, d + 1)])
        elif u == d:
            res.extend([matrix[d][j] for j in range(l, r + 1)])
        return res

//
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return []
        i,j,di,dj = 0,0,0,1
        m, n = len(matrix),len(matrix[0])
        for v in range(m * n):
            res.append(matrix[i][j])
            matrix[i][j] = ''
            if matrix[(i+di)%m][(j+dj)%n] == '':
                di, dj = dj, -di
            i += di
            j += dj
        return res