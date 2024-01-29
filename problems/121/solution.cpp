// Accepted: 82ms (95.38%), 93.75MB (29.48%)

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPrice = prices[0];
        int maxProfitVal = 0;
        for (int price : prices) {
            minPrice = min(minPrice, price);
            maxProfitVal = max(maxProfitVal, price - minPrice);
        }

        return maxProfitVal;
    }
};
