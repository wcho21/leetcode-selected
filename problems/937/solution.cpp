// Accepted: 8ms (69.71%), 13.92MB (19.95%)

class Solution {
public:
    vector<string> reorderLogFiles(vector<string>& logs) {
        unordered_map<string, pair<int, pair<string, string>>> keys;
        auto getKey = [&keys](const string& log) {
            if (keys.count(log) != 0) {
                return keys[log];
            }

            int i = log.find(" ");
            string identifier = log.substr(0, i);
            string content = log.substr(i+1);

            if (isdigit(content[0])) {
                keys[log] = {1, {"", ""}};
                return keys[log];
            }
            keys[log] = {0, {content, identifier}};
            return keys[log];
        };

        stable_sort(logs.begin(), logs.end(), [&getKey](const string& s1, const string& s2) {
            return getKey(s1) < getKey(s2);
        });

        return logs;
    }
};
