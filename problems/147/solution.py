# Accepted: 537ms (16.64%), 18.38MB (96.23%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initialize sorted list as dummy node
        sortedBeg = ListNode()

        node = head # rename

        while node is not None:
            oldHeadNext = node.next

            s = sortedBeg
            while True:
                # if end, insert node
                if s.next == None:
                    s.next = node
                    node.next = None
                    break

                if node.val > s.next.val:
                    s = s.next
                    continue

                # insert node if node.val <= s.next.val
                oldNext = s.next
                s.next = node
                node.next = oldNext
                break

            node = oldHeadNext

        return sortedBeg.next
