// Accepted: 13ms (52.20%), 17.23MB (6.26%)

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counts;
        for (int num : nums) {
            ++counts[num];
        }

        unordered_map<int, vector<int>> countToNums;
        for (auto& [num, count] : counts) {
            countToNums[count].push_back(num);
        }

        vector<int> tops;
        for (int count = nums.size(); count > 0; --count) {
            if (countToNums.count(count) == 0) {
                continue;
            }

            for (int num : countToNums[count]) {
                tops.push_back(num);
                --k;
            }

            if (k <= 0) {
                break;
            }
        }

        return tops;
    }
};
