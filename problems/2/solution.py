# Accepted: 49ms (97.07%), 17.50MB (7.50%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Head = l1
        l2Head = l2

        # swap if l2 is longer
        while l1 is not None and l2 is not None:
            l1 = l1.next
            l2 = l2.next
        if l1 is None and l2 is not None:
            l1Head, l2Head = l2Head, l1Head

        l1 = l1Head
        l2 = l2Head

        # add l2 numbers to l1 numbers
        carry = 0
        while l1 is not None or l2 is not None:
            # add
            added = 0
            added += l1.val
            if l2 is not None:
                added += l2.val
            added += carry
            carry = 0

            # udpate node and carry
            carry, added = divmod(added, 10)
            l1.val = added

            # advance
            l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if carry == 0:
            return l1Head

        # append carry node if nonzery carry
        l1 = l1Head
        while l1 is not None and l1.next is not None:
            l1 = l1.next
        l1.next = ListNode(carry)

        return l1Head
