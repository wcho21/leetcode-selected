# Accepted: 35ms (96.44%), 19.26MB (30.02%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        oddNode, evenNode = oddHead, evenHead = head, head.next

        while evenNode is not None and evenNode.next is not None:
            # reorder
            oddNode.next = evenNode.next
            evenNode.next = evenNode.next.next

            # advance
            oddNode = oddNode.next
            evenNode = evenNode.next

        # append even-index nodes to odd-index ones
        oddNode.next = evenHead
        return oddHead
