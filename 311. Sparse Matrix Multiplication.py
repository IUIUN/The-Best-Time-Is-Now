class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        r1, c1 = len(A), len(A[0])
        r2,c2 = len(B), len(B[0]) 
        res = [[0 for _ in range(c2)] for _ in range(r1)]
        for i in range(r1):
            for j in range(c1):
                if A[i][j]:
                    for k in range(c2):
                        res[i][k] += A[i][j]*B[j][k]
        return res