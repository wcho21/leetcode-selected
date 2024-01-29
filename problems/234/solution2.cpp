// Accepted: 136ms (98.18%), 110.68MB (99.30%)

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode *prev, *slow, *fast;
        prev = nullptr;
        slow = fast = head;

        // place slow runner at the middle and reverse the first half
        while (fast != nullptr && fast->next != nullptr) {
            ListNode* oldSlow = slow;

            // advance
            slow = slow->next;
            fast = fast->next->next;

            oldSlow->next = prev; // reverse
            prev = oldSlow;
        }

        // advance slow if odd number of nodes
        if (fast != nullptr) {
            slow = slow->next;
        }

        ListNode* reverse = prev;
        ListNode* forward = slow;

        // return false if not palindrome; true otherwise
        while (reverse != nullptr && forward != nullptr) {
            if (reverse->val != forward->val) {
                return false;
            }

            reverse = reverse->next;
            forward = forward->next;
        }
        return true;
    }
};
