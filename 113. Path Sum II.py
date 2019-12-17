# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        self.helper(root, [], res, sum)
        return res
    def helper(self, root, ls, res, sum):
        if not root.left and not root.right and root.val == sum:
            ls.append(root.val)
            res.append(ls)
        if root.left:
            self.helper(root.left, ls+[root.val], res, sum - root.val)
        if root.right:
            self.helper(root.right, ls+[root.val], res, sum - root.val)
