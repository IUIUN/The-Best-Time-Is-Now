# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.leng = 0
        self.depth(root)
        return self.leng
    def depth(self, node):
        if not node:
            return 0
        left = self.depth(node.left)
        right = self.depth(node.right)
        self.leng = max(self.leng, left + right)
        print(self.leng)
        return 1 + max(left, right)
        
        
    
    
         