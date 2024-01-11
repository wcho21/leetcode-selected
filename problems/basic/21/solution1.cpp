// Accepted: 6ms (47.93%), 15.13MB (45.84%)

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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode mergedDummyHead = ListNode();
        ListNode* merged = &mergedDummyHead;

        while (list1 != nullptr && list2 != nullptr) {
            if (list1->val < list2->val) {
                merged->next = list1;
                merged = merged->next;
                list1 = list1->next;
            } else {
                merged->next = list2;
                merged = merged->next;
                list2 = list2->next;
            }
        }

        while (list1 != nullptr) {
            merged->next = list1;
            merged = merged->next;
            list1 = list1->next;
        }
        while (list2 != nullptr) {
            merged->next = list2;
            merged = merged->next;
            list2 = list2->next;
        }

        return mergedDummyHead.next;
    }
};
