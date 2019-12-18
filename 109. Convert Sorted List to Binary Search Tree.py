# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
        return self.helper(ls, 0, len(ls)-1)
    def helper(self, ls, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(ls[start])
        mid = (start + end)//2
        root = TreeNode(ls[mid])
        root.left = self.helper(ls, start, mid-1)
        root.right = self.helper(ls, mid + 1, end)
        return root
        
       