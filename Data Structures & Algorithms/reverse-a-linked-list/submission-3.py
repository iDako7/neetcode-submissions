# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # two pointer
        pre, cur = None, head

        while cur:
            # temp for iteration
            temp = cur.next

            # next become previous
            cur.next = pre

            # move to next nodex
            pre = cur
            cur = temp
        
        return pre
        