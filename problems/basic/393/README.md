# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [393. UTF-8 Validation][problem]

[problem]: https://leetcode.com/problems/utf-8-validation/description/



## How to solve

What the problem asks to do is straightforward and simple.
Simply check the prefix bits for each byte.



## Complexities

Suppose that the input list of numbers (bytes) has a length of $N$.

### Time

We visit bytes $O(1)$ times.
Thus, $O(N)$.


### Space

Extra space required no more than $O(1)$.
