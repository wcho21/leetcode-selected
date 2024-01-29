// Accepted: 3ms (81.58%), 9.77MB (5.42%)

class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        transform(paragraph.begin(), paragraph.end(), paragraph.begin(), [](const unsigned char& ch) {
            return isalpha(ch) ? (unsigned char)tolower(ch) : ' ';
        });

        vector<string> words;
        stringstream ss(paragraph);
        string s;
        while (ss >> s) {
            words.push_back(s);
        }

        unordered_map<string, int> counts;
        for (string word : words) {
            counts[word]++;
        }

        unordered_set<string> bannedSet(banned.begin(), banned.end());

        string mostCommonWord;
        int mostCommonCount = 0;
        for (auto& [word, count] : counts) {
            if (bannedSet.count(word) != 0) {
                continue;
            }
            if (count <= mostCommonCount) {
                continue;
            }

            mostCommonCount = count;
            mostCommonWord = word;
        }

        return mostCommonWord;
    }
};
