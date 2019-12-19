class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        for x in [A[0], B[0]]:
            if all(x in d for d in zip(A, B)):
                return (len(A) - max(A.count(x), B.count(x)))
        return -1
        
    
        