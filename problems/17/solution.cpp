// Accepted: 3ms (42.04%), 6.90 (70.21%)

class Solution {
    unordered_map<char, string> digitToLetters {
        {'2', "abc"},
        {'3', "def"},
        {'4', "ghi"},
        {'5', "jkl"},
        {'6', "mno"},
        {'7', "pqrs"},
        {'8', "tuv"},
        {'9', "wxyz"},
    };
    vector<string> getCombinations(const string& digits, const int i = 0) {
        if (i == digits.size()) {
            return {""};
        }

        char digit = digits[i];
        string letters = digitToLetters[digit];

        vector<string> combinations;
        for (const string& toCombine : getCombinations(digits, i+1)) {
            for (const char& letter : letters) {
                combinations.push_back(letter+toCombine);
            }
        }

        return combinations;
    }
public:
    vector<string> letterCombinations(string digits) {
        if (digits.size() == 0) {
            return {};
        }

        return getCombinations(digits);
    }
};
