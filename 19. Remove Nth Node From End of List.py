# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        res = ListNode(0)
        res.next = head
        slow = res
        fast = res
        for i in range(0,n+1):
            fast = fast.next
        while fast != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return res.next