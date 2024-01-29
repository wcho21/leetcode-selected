# Accepted: 38ms (63.78%), 17.37MB (32.01%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or left == right:
            return head

        dummyHead = ListNode(0, head)

        # find the first node to reverse, which becomes the last node in the reversed list
        prev = dummyHead
        node = head

        for _ in range(left-1):
            prev = node
            node = node.next

        # keep the node just before the reversed list, and the last node in the reversed list
        reversedFirstPrev = prev
        reversedLast = node

        # reverse the given interval
        prev = node
        node = node.next
        for _ in range(right-left):
            oldNodeNext = node.next

            # reverse
            node.next = prev

            # advance
            prev = node
            node = oldNodeNext

        # keep the first node in the reversed list, and the node just after the reversed list
        reversedFirst = prev
        reversedLastNext = node

        # complete the list
        reversedFirstPrev.next = reversedFirst
        reversedLast.next = reversedLastNext

        return dummyHead.next
