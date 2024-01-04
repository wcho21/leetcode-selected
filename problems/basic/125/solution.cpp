// Accepted: 4ms (80.77%), 8.12MB (11.46%)

class Solution {
public:
    bool isPalindrome(string s) {
        string filtered;
        for (char ch : s) {
            if (!isalnum(ch)) {
                continue;
            }

            filtered.push_back(tolower(ch));
        }

        for (int i = 0; i < filtered.size(); ++i) {
            int j = filtered.size()-1-i;
            if (filtered[i] != filtered[j]) {
                return false;
            }
        }
        return true;
    }
};
