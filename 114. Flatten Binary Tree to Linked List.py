# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        left = root.left
        right = root.right
        root.left = None
        self.flatten(left)
        self.flatten(right)
        root.right = left
        while root.right:
            root = root.right
        root.right = right
            
        
        
