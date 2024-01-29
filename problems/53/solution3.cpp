// Accepted: 87ms (46.54%), 70.18MB (15.69%)

class Solution {
public:
    int go(const vector<int>& nums, int left, int right) {
        int diff = right - left;
        if (diff == 1) {
            return nums[left];
        }
        if (diff <= 0) {
            throw std::runtime_error("not positive diff");
        }

        int mid = left + diff/2;

        int leftSum = nums[mid-1];
        int leftMax = leftSum;
        for (int i = mid-2; i >= left; --i) {
            leftSum += nums[i];
            leftMax = max(leftMax, leftSum);
        }

        int rightSum = nums[mid];
        int rightMax = rightSum;
        for (int i = mid+1; i < right; ++i) {
            rightSum += nums[i];
            rightMax = max(rightMax, rightSum);
        }

        int crossedMax = leftMax + rightMax;

        int maxSum = max(go(nums, left, mid), go(nums, mid, right));
        maxSum = max(maxSum, crossedMax);
        return maxSum;
    }

    int maxSubArray(vector<int>& nums) {
        return go(nums, 0, nums.size());
    }
};
