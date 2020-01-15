
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.res = 0
        self.dfs(root, L, R, self.res)
        return self.res
    
    def dfs(self, root, L, R, res):
        if not root:
            return
        if L <= root.val <= R:
            self.res += root.val
        if root.val < R:
            self.dfs(root.right, L, R, self.res)
        if root.val > L:
            self.dfs(root.left, L, R, self.res)