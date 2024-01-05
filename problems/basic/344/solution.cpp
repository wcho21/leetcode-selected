// Accepted: 23ms (28.43%), 23.56MB (62.58%)

class Solution {
public:
    void reverseString(vector<char>& s) {
        int mid = s.size()/2;
        int end = s.size()-1;

        for (int i = 0; i < mid; ++i) {
            char temp = s[i];
            s[i] = s[end-i];
            s[end-i] = temp;
        }
    }
};
