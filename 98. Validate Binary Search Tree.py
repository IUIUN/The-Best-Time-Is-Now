# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(float('-inf'), float('inf'), root)
    
    def helper(self, lowerBound, upperBound, root):
        if not root:
            return True
        if root.val <= lowerBound or root.val >= upperBound:
            return False
        left = self.helper(lowerBound, root.val, root.left)
        right = self.helper(root.val, upperBound, root.right)
        return left and right
     
        

        
        