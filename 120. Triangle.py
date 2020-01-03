class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
       
        if not triangle:
            return 
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]
        

//状态压缩 使用一维数组
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return None
        mini = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                mini[j] = min(mini[j+1], mini[j]) + triangle[i][j]
                print(mini[j])
        return mini[0]
        