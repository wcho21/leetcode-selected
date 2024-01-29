// Accepted: 0ms (100.00%), 7.78MB (62.47%)

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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (head == nullptr || left == right) {
            return head;
        }

        ListNode dummyHead(0, head);

        // find the first node to reverse, which becomes the last node in the reversed list
        ListNode *prev, *node;
        prev = &dummyHead;
        node = head;

        for (int i = 0; i < left-1; ++i) {
            prev = node;
            node = node->next;
        }

        // keep the node just before the reversed list, and the last node in the reversed list
        ListNode *reversedFirstPrev, *reversedLast;
        reversedFirstPrev = prev;
        reversedLast = node;

        // reverse the given interval
        prev = node;
        node = node->next;
        for (int i = 0; i < right-left; ++i) {
            ListNode* oldNodeNext = node->next;

            // reverse
            node->next = prev;

            // advance
            prev = node;
            node = oldNodeNext;
        }

        // keep the first node in the reversed list, and the node just after the reversed list
        ListNode *reversedFirst, *reversedLastNext;
        reversedFirst = prev;
        reversedLastNext = node;

        // complete the list
        reversedFirstPrev->next = reversedFirst;
        reversedLast->next = reversedLastNext;

        return dummyHead.next;
    }
};
