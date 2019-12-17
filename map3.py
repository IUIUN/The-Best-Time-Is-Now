def getMininumUniqueSum(arr):
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            arr[i] = arr[i-1]+1
    return sum(arr)

if __name__ == "__main__":
    arr = [3,2,1,2,7]
    print(getMininumUniqueSum(arr))