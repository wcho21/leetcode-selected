// Accepted: 0ms (100.00%), 7.60MB (11.69%)

class Solution {
    int counts['z'+1];
public:
    int numJewelsInStones(string jewels, string stones) {
        for (char stone : stones) {
            ++counts[stone];
        }

        int numJewels = 0;
        for (char jewel : jewels) {
            numJewels += counts[jewel];
        }
        return numJewels;
    }
};
