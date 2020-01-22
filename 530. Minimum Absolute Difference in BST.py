# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    res = float('inf')
    pre = -float('inf')
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root:
            return None
        if root.left:
            self.getMinimumDifference(root.left)
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        if root.right:
            self.getMinimumDifference(root.right)
        return self.res
        