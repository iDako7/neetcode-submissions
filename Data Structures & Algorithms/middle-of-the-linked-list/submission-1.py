# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # while slow and fast
            # fast move two times than slow

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

        # step fast slow
        # 1 2 3
        # 2 3 5
        # 3 4 none