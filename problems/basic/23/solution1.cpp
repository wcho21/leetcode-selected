// Accepted: 11ms (92.74%), 17.67MB (17.27%)

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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<int, vector<int>, greater<int>> queue;

        for (ListNode* node : lists) {
            while (node != nullptr) {
                queue.push(node->val);
                node = node->next;
            }
        }

        ListNode mergedHead;
        ListNode *cur = &mergedHead;
        while (!queue.empty()) {
            int val = queue.top();
            queue.pop();
            cur->next = new ListNode(val);
            cur = cur->next;
        }

        return mergedHead.next;
    }
};
