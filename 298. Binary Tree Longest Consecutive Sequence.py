# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        
        return self.dfs(root, None, 0 )
    def dfs(self, root, parent, len):
        if not root:
            return len
        if parent != None and root.val == parent.val + 1:
            len += 1
        else:
            len = 1
        return max(len, max(self.dfs(root.left, root, len), self.dfs(root.right, root, len)))
        