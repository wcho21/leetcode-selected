// Accepted: 211ms (23.94%), 128.80MB (20.06%)

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
        vector<int> vals;
        for (ListNode* node = head; node != nullptr; node = node->next) {
            vals.push_back(node->val);
        }

        // return false if not palindrome; return true otherwise
        for (int i = 0; i < vals.size() / 2; ++i) {
            if (vals[i] != vals[vals.size()-1-i]) {
                return false;
            }
        }
        return true;
    }
};
