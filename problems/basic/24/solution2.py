# Accepted: 41ms (44.87%), 17.25MB (21.85%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        left, right = head, head.next
        left.next = self.swapPairs(right.next)
        right.next = left

        return right
