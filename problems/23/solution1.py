# Accepted: 71ms (96.92%), 20.80MB (16.92%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        queue = []

        for nodeList in lists:
            node = nodeList
            while node is not None:
                heappush(queue, node.val)
                node = node.next

        cur = mergedHead = ListNode(0)
        while len(queue) > 0:
            val = heappop(queue)
            cur.next = ListNode(val)
            cur = cur.next

        return mergedHead.next
