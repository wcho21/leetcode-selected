// Accepted: 128ms (90.54%), 101.52MB (63.65%)

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> daysToWait(temperatures.size(), 0);
        vector<int> stack;

        for (int day = 0; day < temperatures.size(); ++day) {
            while (stack.size() > 0) {
                int pastDay = stack.back();
                int pastTemp = temperatures[pastDay];
                int curTemp = temperatures[day];

                if (pastTemp >= curTemp) {
                    break;
                }

                daysToWait[pastDay] = day - pastDay;
                stack.pop_back();
            }

            stack.push_back(day);
        }

        return daysToWait;
    }
};
