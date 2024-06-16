# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(head1, head2):
            dummyHead = ListNode()
            cur = dummyHead

            while head1 is not None or head2 is not None:
                if head1 is None:
                    cur.next = head2
                    cur = cur.next
                    head2 = head2.next
                    continue

                if head2 is None:
                    cur.next = head1
                    cur = cur.next
                    head1 = head1.next
                    continue

                if head1.val <= head2.val:
                    cur.next = head1
                    head1 = head1.next
                else:
                    cur.next = head2
                    head2 = head2.next
                cur = cur.next

            return dummyHead.next

        def halveAndGetMid(head):
            if head is None or head.next is None:
                return None

            prevSlow = None
            slow = head
            fast = head

            while fast is not None and fast.next is not None:
                prevSlow = slow
                slow = slow.next
                fast = fast.next.next

            prevSlow.next = None # halve

            return slow # mid

        def mergeSort(head):
            if head is None or head.next is None:
                return head

            mid = halveAndGetMid(head)
            mergedLower = mergeSort(head)
            mergedUpper = mergeSort(mid)
            merged = merge(mergedLower, mergedUpper)
            return merged

        return mergeSort(head)
