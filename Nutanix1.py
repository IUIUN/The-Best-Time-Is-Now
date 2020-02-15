def countWays(are, n): 
    pos = [0 for i in range(n)] 
    p = 0
  
    # for loop for saving the positions 
    # of all 1s 
    for i in range(n): 
        if (arr[i] == 1): 
            pos[p] = i + 1
            p += 1
  
    # If array contains only 0s 
    if (p == 0): 
        return 0
  
    ways = 1
    for i in range(p - 1): 
        ways *= pos[i + 1] - pos[i] 
  
    # Return the total ways 
    return ways 
  
# Driver code 
if __name__ == '__main__': 
    arr = [1, 0, 1, 0, 1] 
    n = len(arr) 
    print(countWays(arr, n)) 
      
# This code is contr