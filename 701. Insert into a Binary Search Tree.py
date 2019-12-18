# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        self.helper(root, val)
        return root
    
    def helper(self, root, val):
        if not root:
            return TreeNode(val)
        if root.val < val:
            root.right = self.helper(root.right, val)
        if root.val > val:
            root.left = self.helper(root.left, val)
        return root
            
            
        