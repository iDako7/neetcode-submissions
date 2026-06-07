# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        91
        21

        9 + 2 = 10, 1
        1 + 1 + carry = 3
        '''
        # initialize carry, new list
        # p1 p2 pointers for two linked list
        # move both pointer forward until both to end
            # caculation handle carry
        
        carry = 0
        dummy = ListNode()
        cur = dummy

        # forget to check carry exist, if carry exist, we need to create new node
        while l1 or l2 or carry:
            # check whether l1 and l2 exist
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # caculate value
            val = v1 + v2 + carry
            if val >= 10:
                carry = 1
                val = val - 10
            else:
                carry = 0

            # create new node and assign to dummy next
            # d node
            #   
            node = ListNode(val)
            cur.next = node
            
            # update cur to next node
            # why we could not assign cur to node ??
            cur = cur.next
            # error: don't update l1 and l2
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next

