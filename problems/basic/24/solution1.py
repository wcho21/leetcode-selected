# Accepted: 37ms (70.07%), 17.28MB (21.85%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        dummyHead = ListNode(0, head)

        prev = dummyHead
        left, right = head, head.next

        while True:
            # swap
            oldRightNext = right.next
            prev.next = right
            right.next = left
            left.next = oldRightNext

            if oldRightNext is None or oldRightNext.next is None:
                break

            # advance
            prev = left
            left = oldRightNext
            right = oldRightNext.next

        return dummyHead.next
