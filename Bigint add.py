def findSum(str1, str2): 
  
    # Before proceeding further, make sure length 
    # of str2 is larger. 
    if len(str1)> len(str2): 
        str1, str2 = str2, str1 
   
    # Take an empty string for storing result 
    str3 = "" 
   
    # Calculate length of both string 
    n1 = len(str1) 
    n2 = len(str2) 
    diff = n2 - n1 
   
    # Initially take carry zero 
    carry = 0
   
    # Traverse from end of both strings 
    for i in range(n1-1,-1,-1): 
      
        # Do school mathematics, compute sum of 
        # current digits and carry 
        
        sum = ((ord(str1[i])-ord('0')) +
                   int((ord(str2[i+diff])-ord('0'))) + carry) 
       
        str3 = str3+str(sum%10 ) 
          
         
        carry = sum//10
   
    # Add remaining digits of str2[] 
    for i in range(n2-n1-1,-1,-1): 
      
        sum = ((ord(str2[i])-ord('0'))+carry) 
        str3 = str3+str(sum%10 ) 
        carry = sum//10
   
    # Add remaining carry 
    if (carry): 
        str3+str(carry+'0') 
   
    # reverse resultant string 
    str3 = str3[::-1] 
   
    return str3 
   
# Driver code 
if __name__ == "__main__": 
    str1 = "12"
    str2 = "198111"
    print(findSum(str1, str2)) 
  