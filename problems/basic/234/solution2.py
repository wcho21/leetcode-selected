# Accepted: 284ms (97.92%), 28.01MB (99.48%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = None
        slow = fast = head

        # place slow runner at the middle and reverse the first half
        while fast is not None and fast.next is not None:
            oldSlow = slow

            # advance
            slow = slow.next
            fast = fast.next.next

            oldSlow.next = prev # reverse
            prev = oldSlow

        # advance slow if odd number of nodes
        if fast is not None:
            slow = slow.next

        reverse = prev
        forward = slow

        # return false if not palindrome; true otherwise
        while reverse is not None and forward is not None:
            if reverse.val != forward.val:
                return False

            reverse = reverse.next
            forward = forward.next

        return True
