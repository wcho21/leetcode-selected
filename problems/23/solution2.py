# Accepted: 83ms (69.15%), 20.31MB (39.09%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def go(lists: List[Optional[ListNode]], left: int = 0, right: int = len(lists)):
            diff = right - left
            if diff == 0:
                return None
            if diff == 1:
                return lists[left]

            mid = left + diff // 2
            mergedLeft = go(lists, left, mid)
            mergedRight = go(lists, mid, right)

            return merge(mergedLeft, mergedRight)

        def merge(left: Optional[ListNode], right: Optional[ListNode]):
            if left is None:
                return right
            if right is None:
                return left

            if left.val < right.val:
                left.next = merge(left.next, right)
                return left
            else:
                right.next = merge(left, right.next)
                return right

        return go(lists)
