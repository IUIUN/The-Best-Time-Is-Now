def helper(arr, start, end, mem, operation, preSum):
        if start == end:
                if operation == 1:
                        return arr[start]
                else:
                        return -arr[start]
        if mem[start][end] != -1:
                return mem[start][end]
        if operation == 1:
                mem[start][end] = preSum[start][end] + max(helper(arr, start+1,end, mem, 0, preSum), helper(arr, start,end-1, mem, 0, preSum))
        else:
                mem[start][end] = -preSum[start][end] + max(helper(arr, start+1,end, mem, 1, preSum), helper(arr, start,end-1, mem, 1, preSum))
        return mem[start][end]

def  maxScore(arr):
        n = len(arr)
        preSum = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
                for j in range(i,n):
                        if i == j:
                                preSum[i][j] = arr[i]
                        else:
                                preSum[i][j] = preSum[i][j-1] + arr[j]
        mem = [[-1 for _ in range(n)] for _ in range(n)]
        return helper(arr, 0, n-1, mem, 1, preSum)

if __name__ == "__main__":
        arr = [1,2,3,4,2,6]
        n = len(arr)
        preSum = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
                for j in range(i,n):
                        if i == j:
                                preSum[i][j] = arr[i]
                        else:
                                preSum[i][j] = preSum[i][j-1] + arr[j]
        print(preSum)
        mem = [[-1 for _ in range(n)] for _ in range(n)]
        print(maxScore(arr))