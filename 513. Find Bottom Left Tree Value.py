# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return None
        queue = [root]
        while queue:
            node = queue.pop(0)
            res = node.val
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return res
    