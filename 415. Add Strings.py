class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        nums1 = list(num1)
        nums2 = list(num2)
        carry, res = 0, []
        while len(nums1) > 0 or len(nums2) > 0:
            n1 = ord(nums1.pop()) - ord("0") if len(nums1) > 0 else 0
            n2 = ord(nums2.pop()) - ord("0") if len(nums2) > 0 else 0
            n = n1 + n2 + carry
            carry = n //10
            res.append(n%10)
        if carry:
            res.append(carry)
        
        return "".join(str(i) for i in res)[::-1]
        
            
        
       