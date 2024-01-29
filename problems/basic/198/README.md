# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [198. House Robber][problem]

[problem]: https://leetcode.com/problems/house-robber/description/



## How to solve

We're going to construct an array that stores the maximum amount of money to rob.

Suppose that we've calculated the answers in the array `robbed` up to index `n-1`.
To determine `robbed[n]`, simply pick the maximum of `robbed[n-1]` and `robbed[n-2] + money[n]`.
That is, comparing the case of not robbing the money in the current house (`robbed[n-1]`) with the case of robbing (`robbed[n-2] + money[n]`).
Then the answer is the maximum amount of money in the array `robbed`.


## Complexities

Suppose that the input array has a length of $N$.

### Time

Since we visit each number $O(1)$ times, it takes $O(N)$ time.

### Space

An array to store the maximums take $O(N)$ space.
