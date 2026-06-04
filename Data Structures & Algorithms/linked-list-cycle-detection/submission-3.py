# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        count = 0


        # the fast pointer will meet slow pointer eventually, if there is a cycle

        while fast and fast.next:
            # error: check before move then always true
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
            
        return False