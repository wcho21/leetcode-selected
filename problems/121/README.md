# README

![Difficulty Easy](https://img.shields.io/badge/Difficulty-Easy-green)

Problem: [121. Best Time to Buy and Sell Stock][problem]

[problem]: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/


## How to solve

For each number, we keep the least number so far.
The maximum profit is the difference between the current number and the least number.



## Complexities

Suppose that the list of input numbers has a length of $N$.

### Time

It visits each number, so $O(N)$.

### Space

Only $O(1)$ space required.
