class Solution:
    def maxPathSum(self, root):
        self.ans =  -sys.maxsize - 1
        self.helper(root)
        return self.ans 
    
    def helper(self, root):
        if not root:
            return -sys.maxsize - 1
        l = max(0, self.helper(root.left))
        r = max(0, self.helper(root.right))
        self.ans = max(self.ans, root.val + l + r)
        return root.val + max(l, r)