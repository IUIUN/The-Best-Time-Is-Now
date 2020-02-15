def printKMissing(arr, k) : 
      
    i = 0
    count = 0
    curr = arr[0]
    n = arr[-1]
    if k > arr[-1] - arr[0] - len(arr) + 1:
        return None
    while (count < k and i < n) :  
        if (arr[i] != curr) : 
            count = count + 1
        else: 
            i = i + 1
          
        curr = curr + 1
    if count == k:
        return curr-1
    else:
        return None


if __name__ == "__main__":
    a = [-1,2,5,6,8,9]
    k = 5
    print(printKMissing(a, k))
