# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        method 1: use a set to trace
        method 2: two pointers with slow and fast
        '''

        slow, fast = head, head

        # we should check whether fast.next.next exist since we to use
        # .next.next to iterate
        # error: fast.next.next and fast.next. fast.next.next depends on fast and fast.next
        while fast and fast.next:
            # move first
            slow = slow.next
            fast = fast.next.next
            
            # check if fast == slow, then there is a loop
            if fast == slow:
                return True
        return False