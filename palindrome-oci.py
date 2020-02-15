def isPalidrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True
def longestPalidrome(s):
    if len(s)==0:
        	return ""
    maxLen=1
    start=0
    for i in range(len(s)):
        if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
            start=i-maxLen-1
            maxLen+=2
            continue

        if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
            start=i-maxLen
            maxLen+=1
    return s[start:start+maxLen]
#     if not isPalidrome(s):
#         res = ""
#         for i in range(len(s)):
#             t1 = helper(s, i, i)
#             if len(t1) > len(res):
#                 res = t1
#             t2 = helper(s, i, i + 1)
#             if len(t2) > len(t1):
#                 res = t2
#         return res
#     else:
#         return s

# def helper(s, l, r):
#     while l >=0 and r <= len(s) - 1 and s[l] ==s[r]:
#         l -= 1
#         r += 1
#     return s[l + 1: r]


            



if __name__ == "__main__":
    s1 = ""
    s2 = "1234567"
    s3 = "1234321"
    s4 = "a"
    s5 = "1a2bb32a1 ,"
    print(longestPalidrome(s1))
    print(longestPalidrome(s2))
    print(longestPalidrome(s3))
    print(longestPalidrome(s4))
    print(longestPalidrome(s5))


