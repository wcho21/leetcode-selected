// Accepted: 4ms (41.68%), 7.78MB (93.40%)

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
    ListNode* swapPairs(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return head;
        }

        ListNode *left, *right;
        left = head;
        right = head->next;

        left->next = swapPairs(right->next);
        right->next = left;

        return right; // as a new head
    }
};
