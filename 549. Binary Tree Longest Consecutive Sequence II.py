# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
     def longestConsecutive(self, root: TreeNode) -> int:
        def longest_path(root):
            if not root:
                return 0, 0
            inc, dec = 1, 1
            l_inc, l_dec = longest_path(root.left)
            r_inc, r_dec = longest_path(root.right)
            if root.left:
                if root.left.val == root.val + 1:
                    inc = max(inc, l_inc + 1)
                if root.left.val == root.val - 1:
                    dec = max(dec, l_dec + 1)
            if root.right:
                if root.right.val == root.val + 1:
                    inc = max(inc, r_inc + 1)
                if root.right.val == root.val - 1:
                    dec = max(dec, r_dec + 1)
            res[0] = max(res[0], inc + dec - 1)
            return (inc, dec)
        res = [0]
        longest_path(root)
        return res[0]
    