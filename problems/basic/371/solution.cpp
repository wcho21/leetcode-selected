// Accepted: 2ms (48.94%), 6.50MB (17.47%)

class Solution {
public:
    int getSum(int a, int b) {
        while (true) {
            int carry = (a & b) << 1;
            int added = a ^ b;

            if (carry == 0) {
                return added;
            }

            a = carry;
            b = added;
        }
    }
};
