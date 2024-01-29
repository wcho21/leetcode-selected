// Accepted: 0ms (100.00%), 6.54MB (97.55%)

class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;

        for (char c : s) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push_back(c);
                continue;
            }

            // return false if unmatched closing parenthesis
            if (stack.size() == 0) {
                return false;
            }

            char pop = stack.back();
            stack.pop_back();

            if (c == ')' && pop != '(') {
                return false;
            }
            if (c == '}' && pop != '{') {
                return false;
            }
            if (c == ']' && pop != '[') {
                return false;
            }
        }

        // return false if any unmatched opening parenthesis
        if (stack.size() != 0) {
            return false;
        }

        return true;
    }
};
