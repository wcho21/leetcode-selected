# Accepted: 38ms (77.10%), 18.65MB (18.46%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: Optional[ListNode], prev: Optional[ListNode] = None) -> Optional[ListNode]:
            if node is None:
                return prev

            oldNext = node.next

            node.next = prev # reverse

            # return the head of the reversed list
            return reverse(oldNext, node)

        return reverse(head)
