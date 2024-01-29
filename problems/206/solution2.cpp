// Accepted: 7ms (36.37%), 8.74MB (29.19%)

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
    ListNode* reverse(ListNode* node, ListNode* prev = nullptr) {
        if (node == nullptr) {
            return prev;
        }

        ListNode* oldNext = node->next;

        node->next = prev; // reverse

        // return the head of the reversed list
        return reverse(oldNext, node);
    }
public:
    ListNode* reverseList(ListNode* head) {
        return reverse(head);
    }
};
