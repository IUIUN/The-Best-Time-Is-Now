# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)
    
    def dfs(self, root, p, q):
        if not root:
            return None
        if root == p or root ==q:
            return root
        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)
        
        if left and right:
            return root
        if not left:
            return right
        else:
            return left
        
            
        
            
        