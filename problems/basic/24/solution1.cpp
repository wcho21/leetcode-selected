// Accepted: 4ms (41.68%), 7.97MB (23.99%)

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

        ListNode dummyHead(0, head);

        ListNode *prev, *left, *right;
        prev = &dummyHead;
        left = head;
        right = head->next;

        while (true) {
            // swap
            ListNode* oldRightNext = right->next;
            prev->next = right;
            right->next = left;
            left->next = oldRightNext;

            if (oldRightNext == nullptr || oldRightNext->next == nullptr) {
                break;
            }

            // advance
            prev = left;
            left = oldRightNext;
            right = oldRightNext->next;
        }

        return dummyHead.next;
    }
};
