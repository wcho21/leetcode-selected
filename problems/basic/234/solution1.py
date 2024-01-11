# Accepted: 307ms (90.79%), 37.37MB (81.55%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        numbers = []

        node = head
        while node is not None:
            numbers.append(node.val)
            node = node.next

        for i in range(len(numbers)):
            if numbers[i] != numbers[len(numbers)-1-i]:
                return False
        return True
