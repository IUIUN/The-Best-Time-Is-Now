# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        list_val, list_node = [], []
        self.helper(root, list_val, list_node)
        list_val.sort()
        for i in range(len(list_val)):
            list_node[i].val = list_val[i]
        return root
            
    def helper(self, root, list_val, list_node):
        if not root:
            return
        self.helper(root.left, list_val, list_node)
        list_val.append(root.val)
        list_node.append(root)
        self.helper(root.right, list_val, list_node)
