# Accepted: 39ms (78.39%), 17.48MB (14.10%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedDummyHead = ListNode()
        merged = mergedDummyHead

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                merged.next = list1
                merged = merged.next
                list1 = list1.next
            else:
                merged.next = list2
                merged = merged.next
                list2 = list2.next

        while list1 is not None:
            merged.next = list1
            merged = merged.next
            list1 = list1.next
        while list2 is not None:
            merged.next = list2
            merged = merged.next
            list2 = list2.next

        return mergedDummyHead.next
