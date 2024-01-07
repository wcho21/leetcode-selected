// Accepted: 108ms (100.00%), 88.80 (83.33%)

class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        // xor all
        int xored = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            xored ^= nums[i];
        }

        // count the number of different digits in binary
        int count = 0;
        while (k > 0 || xored > 0) {
            int one1 = k & 1;
            int one2 = xored & 1;

            if (one1 != one2) {
                count++;
            }

            k >>= 1;
            xored >>= 1;
        }

        return count;
    }
};
