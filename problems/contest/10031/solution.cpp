// Accepted: 4ms (83.33%), 19.32MB (33.33%)

class Solution {
public:
    int missingInteger(vector<int>& nums) {
        unordered_set<int> numsSet(nums.begin(), nums.end());

        int seqEnd = 0;
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] == nums[i-1] + 1) {
                seqEnd++;
            } else {
                break;
            }
        }

        int seqSum = 0;
        for (int i = 0; i <= seqEnd; ++i) {
            seqSum += nums[i];
        }

        while (true) {
            if (numsSet.count(seqSum) == 0) {
                return seqSum;
            }
            seqSum++;
        }

        return 0;
    }
};
