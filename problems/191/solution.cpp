// Accepted: 0ms (100.00%), 6.28% (96.36%)

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int dist = 0;
        while (n != 0) {
            if ((n & 1) == 1) {
                dist++;
            }
            n >>= 1;
        }
        return dist;
    }
};

