// Accepted: 73ms (73.78%), 52.30MB (12.35%)

function maxProfit(prices: number[]): number {
    let minPrice = prices[0];
    let maxProfitVal = 0;
    for (const price of prices) {
        minPrice = Math.min(minPrice, price);
        maxProfitVal = Math.max(maxProfitVal, price - minPrice);
    }

    return maxProfitVal;
};
