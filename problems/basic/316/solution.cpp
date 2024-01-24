// Accepted: 3ms (54.61%), 9.52MB (5.04%)

class Solution {
public:
    string removeDuplicateLetters(string s) {
        unordered_map<char, int> lastOccurIndex;
        for (int i = 0; i < s.size(); ++i) {
            char ch = s[i];
            lastOccurIndex[ch] = i;
        }

        unordered_set<char> visited;
        vector<char> ordered;

        for (int i = 0; i < s.size(); ++i) {
            char ch = s[i];

            if (visited.count(ch) != 0) {
                continue;
            }

            // pop characters
            while (ordered.size() > 0) {
                char top = ordered.back();
                if (i >= lastOccurIndex[top]) { // last occurrence
                    break;
                }
                if (ch > top) { // in lexicographical order
                    break;
                }

                visited.erase(top);
                ordered.pop_back();
            }

            // insert current character
            visited.insert(ch);
            ordered.push_back(ch);
        }

        string orderedStr(ordered.begin(), ordered.end());
        return orderedStr;
    }
};
