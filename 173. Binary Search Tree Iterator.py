# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.q = []
        self.allLeftIntoStack(root)
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        
        curr = self.q.pop()
        self.allLeftIntoStack(curr.right)
        return curr.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.q != []
    def allLeftIntoStack(self, root):
        while root:
            self.q.append(root)
            root = root.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()