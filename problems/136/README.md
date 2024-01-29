# README

![Difficulty Easy](https://img.shields.io/badge/Difficulty-Easy-green)

Problem: [136. Single Number][problem]

[problem]: https://leetcode.com/problems/single-number/description/



## How to solve

If XOR operations applied to a number twice, then the number remains unchanged.
Using this fact, do XOR operations on zero with the given numbers.
Since all the duplicate numbers have no effect, only the single number only remains.



## Complexities

Suppose that the input list of numbers has length of $N$.

### Time

Since we visit each number once, we need $O(N)$ time.

### Space

Only $O(1)$ extra space required.
