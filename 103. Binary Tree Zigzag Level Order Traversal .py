# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, temp, stack, flag = [], [], [root], 1
        while stack:
            for i in range(len(stack)):
                node = stack.pop(0)
                temp += [node.val]
                if node.left:
                    stack += [node.left]
                if node.right:
                    stack += [node.right]
            res += [temp[::flag]]
            temp = []
            flag *=-1
        return res
            
            
        