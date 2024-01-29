// Accepted: 30ms (65.91%), 22.80 (17.49%)

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<string> sortedStrs;
        for (string s : strs) {
            sort(s.begin(), s.end());
            sortedStrs.push_back(s);
        }

        unordered_map<string, vector<string>> anagramMap;
        for (int i = 0; i < strs.size(); ++i) {
            anagramMap[sortedStrs[i]].push_back(strs[i]);
        }

        vector<vector<string>> anagramGroups;
        for (auto [str, group] : anagramMap) {
            anagramGroups.push_back(group);
        }

        return anagramGroups;
    }
};
