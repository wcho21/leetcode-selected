// Accepted: 27ms (39.26%), 71.40MB (95.81%)

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* l1Head = l1;
        ListNode* l2Head = l2;

        // swap if l2 is longer
        while (l1 != nullptr && l2 != nullptr) {
            l1 = l1->next;
            l2 = l2->next;
        }
        if (l1 == nullptr && l2 != nullptr) {
            ListNode* temp = l1Head;
            l1Head = l2Head;
            l2Head = temp;
        }

        l1 = l1Head;
        l2 = l2Head;

        // add l2 numbers to l1 numbers
        int carry = 0;
        while (l1 != nullptr || l2 != nullptr) {
            // add
            int added = 0;
            added += l1->val;
            if (l2 != nullptr) {
                added += l2->val;
            }
            added += carry;
            carry = 0;

            // update node and carry
            l1->val = added % 10;
            carry = added / 10;

            // advance
            l1 = l1->next;
            if (l2 != nullptr) {
                l2 = l2->next;
            }
        }

        if (carry == 0) {
            return l1Head;
        }

        // append carry node if nonzero carry
        l1 = l1Head;
        while (l1 != nullptr && l1->next != nullptr) {
            l1 = l1->next;
        }
        l1->next = new ListNode(carry);

        return l1Head;
    }
};
