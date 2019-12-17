"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(curr):
            head, tail = curr, curr
            if curr.left:
                lhead, ltail = helper(curr.left)
                curr.left = ltail
                ltail.right = curr
                head = lhead
            if curr.right:
                rhead, rtail = helper(curr.right)
                curr.right = rhead
                rhead.left = curr
                tail = rtail
            return head, tail
        if root:
            head, tail = helper(root)
            head.left = tail
            tail.right = head
            return head
        else:
            return None
       
                
            