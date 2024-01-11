// Accepted: 4ms (94.23%), 10.74MB (73.01%)

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
    ListNode* oddEvenList(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return head;
        }

        ListNode *oddHead, *evenHead, *oddNode, *evenNode;
        oddHead = oddNode = head;
        evenHead = evenNode = head->next;

        while (evenNode != nullptr && evenNode->next != nullptr) {
            // reorder
            oddNode->next = evenNode->next;
            evenNode->next = evenNode->next->next;

            // advance
            oddNode = oddNode->next;
            evenNode = evenNode->next;
        }

        // append even-index nodes to odd-index ones
        oddNode->next = evenHead;
        return oddHead;
    }
};
