# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # if root is None:
        #     return 0
        # else:
        #     return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
#         if not root:
#             return 0
#         res = self.dfs(root, 1, [])
#         print(res)
#         return max(res)
#     def dfs(self, root, depth, res):
#         if root.left:
#             self.dfs(root.left, depth + 1,res)
#         if root.right:
#             self.dfs(root.right, depth + 1, res)
#         res.append(depth)
#         return res
        
            
        depth = 0
        stack = [(root, 1)]
        while stack:
            node, leng = stack.pop()
            if not root:
                return 0
            if leng > depth:
                depth = leng
            if node.left:
                stack.append((node.left, leng + 1))
            if node.right:
                stack.append((node.right, leng + 1))
        return depth
    
    
    
     