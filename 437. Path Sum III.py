# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        res = [0]
        que = collections.deque()
        que.append(root)
        while(que):
            node = que.popleft()
            if not node:
                continue
            self.dfs(node, res, 0, sum)
            que.append(node.left)
            que.append(node.right)
        return res[0]
    def dfs(self, root, res, path, target):
        if not root:
            return
        path += root.val
        if path == target:
            res[0] +=1
        self.dfs(root.left, res, path, target)
        self.dfs(root.right, res, path, target)



            
        
            
        