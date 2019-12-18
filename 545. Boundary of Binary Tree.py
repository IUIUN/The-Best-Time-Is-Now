# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root):
        if not root:
            return None
        if not root.left and not root.right:
            return [root.val]
        left_boundry = self.find_left_boundry(root.left)
        leaves = self.find_leaves(root)
        right_boundry = self.find_right_boundry(root.right)
        
        if left_boundry and leaves and left_boundry[-1] == leaves[0]:
            leaves = leaves[1:]
        if leaves and right_boundry and leaves[-1] == right_boundry[-1]:
            leaves = leaves[:-1]
        return [root.val] + left_boundry + leaves + list(reversed(right_boundry))
    def find_left_boundry(self, root):
        left_boundry = []
        while root:
            left_boundry.append(root.val)
            if root.left:
                root = root.left
            elif root.right:
                root = root.right
            else:
                break
        return left_boundry
    def find_leaves(self, root):
        stack = [root]
        leaves = []
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                leaves.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return leaves
    def find_right_boundry(self, root):
        right_boundry = []
        while root:
            right_boundry.append(root.val)
            if root.right:
                root = root.right
            elif root.left:
                root = root.left
            else:
                break
        return right_boundry

