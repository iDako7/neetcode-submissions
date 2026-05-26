# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        pre = None
        cur = head

        while cur:
            temp = cur.next
            # change direction
            cur.next = pre

            # move to next item
            pre = cur
            cur = temp
        return pre

        