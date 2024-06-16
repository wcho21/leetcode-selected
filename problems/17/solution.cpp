// Accepted: 0ms (100.00%), 8.59MB (16.58%)

class Solution {
private:
    unordered_map<char, string> digitToLetters {
        { '2', "abc" },
        { '3', "def" },
        { '4', "ghi" },
        { '5', "jkl" },
        { '6', "mno" },
        { '7', "pqrs" },
        { '8', "tuv" },
        { '9', "wxyz" }
    };

    string digits;
    vector<char> collected;
    vector<string> combs;

    void generateCombinations(int i) {
        if (i >= digits.size()) {
            string comb(collected.begin(), collected.end());
            combs.push_back(comb);
            return;
        }

        char digit = digits[i];
        string letters = digitToLetters[digit];
        for (char l : letters) {
            collected.push_back(l);
            generateCombinations(i+1);
            collected.pop_back();
        }
    }

public:
    vector<string> letterCombinations(string digits) {
        if (digits.size() == 0) {
            return {};
        }

        this->digits = digits;
        this->collected = {};
        this->combs = {};

        generateCombinations(0);

        return combs;
    }
};
