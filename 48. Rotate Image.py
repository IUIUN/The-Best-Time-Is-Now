class Solution:
    def rotate(self, A: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        A.reverse()
        for i in range(len(A)):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]