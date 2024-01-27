// Accepted: 18ms (50.50%), 16.95MB (21.76%)

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
    ListNode* go(const vector<ListNode*>& lists, const int left, const int right) {
        const int diff = right - left;
        if (diff == 0) {
            return nullptr;
        }
        if (diff == 1) {
            return lists[left];
        }

        const int mid = left + diff/2;
        ListNode *mergedLeft, *mergedRight;
        mergedLeft = go(lists, left, mid);
        mergedRight = go(lists, mid, right);

        return merge(mergedLeft, mergedRight);
    }

    ListNode* merge(ListNode* left, ListNode* right) {
        if (left == nullptr) {
            return right;
        }
        if (right == nullptr) {
            return left;
        }

        if (left->val < right->val) {
            left->next = merge(left->next, right);
            return left;
        } else {
            right->next = merge(right->next, left);
            return right;
        }
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        return go(lists, 0, lists.size());
    }
};
