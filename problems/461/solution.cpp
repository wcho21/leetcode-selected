// Accepted: 0ms (100.00%), 6.28% (76.44%)

class Solution {
public:
    int hammingDistance(int x, int y) {
        int xored = x ^ y;
        int dist = 0;
        while (xored > 0) {
            if ((xored & 1) == 1) {
                dist++;
            }
            xored >>= 1;
        }
        return dist;
    }
};
