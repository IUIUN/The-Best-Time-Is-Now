def isPalindrome(s):
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -=1
        return True
def longestPalindrome(s):
        if not s:
            return ''
        if not isPalindrome(s):
            ans = ''
            for i in range(len(s)):
                t1 = helper(s, i, i)
                if len(t1) > len(ans):
                    ans = t1
                t2 = helper(s, i, i + 1)
                if len(t2) > len(t1):
                    ans = t2
            return ans
        else:
            return s
def helper(s, l, r):
    while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l + 1: r]
if __name__ == "__main__":
    s1 = "babadababbabadababbabadababbabadababbabadababbabadaba"
    s2 = " "
    s3 = "aba"
    s4 = "00"
    s5 = ",0,0,"
    print(longestPalindrome(s1))
    print(longestPalindrome(s2))
    print(longestPalindrome(s3))
    print(longestPalindrome(s4))
    print(longestPalindrome(s5))