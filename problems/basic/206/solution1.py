# Accepted: 36ms (86.46%), 18.64MB (18.40%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur is not None:
            oldPrev = prev

            prev = cur
            cur = cur.next

            prev.next = oldPrev

        return prev
