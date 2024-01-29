// Accepted: 3ms (80.00%), 6.91MB (60.00%)

typedef long long ll;

class Solution {
public:
    long long numberOfPowerfulInt(long long start, long long finish, int limit, string s) {
        ll suffix = stoll(s);

        if (finish < suffix) {
            return 0;
        }

        ll divider = 1;
        for (int i = 0; i < s.size(); ++i) {
            divider *= 10;
        }

        // determine upper and lower bounds of interval to count
        ll rem;
        ll lower = start / divider;
        rem = start % divider;
        if (rem > suffix) {
            lower++;
        }

        ll upper = finish / divider;
        rem = finish % divider;
        if (rem < suffix) {
            upper--;
        }

        // count the powerful numbers up to n
        auto count = [&](const ll n) {
            if (n == -1) {
                return 0LL;
            }
            if (n == 0) {
                return 1LL;
            }

            vector<int> digits;
            for (char c : to_string(n)) {
                digits.push_back(c - '0');
            }
            int numDigits = digits.size();

            ll numCount = 0;
            for (int i = 0; i < numDigits; ++i) {
                if (digits[i] > limit) {
                    numCount += (ll)(pow(limit+1, numDigits-i));
                    break;
                }

                numCount += (ll)(digits[i] * pow(limit+1, numDigits-i-1));

                if (i == numDigits-1) {
                    numCount++;
                }
            }

            return numCount;
        };

        return count(upper) - count(lower-1);
    }
};
