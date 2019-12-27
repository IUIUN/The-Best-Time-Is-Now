# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        return self.dfs(root, 0, res)
    def dfs(self, root, level, res):
        if not root:
            return
        if len(res) <= level:
            res.append([])
        res[level].append(root.val)
        self.dfs(root.left, level + 1, res)
        self.dfs(root.right, level + 1, res)
        return res
       