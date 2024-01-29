# README

![Difficulty Easy](https://img.shields.io/badge/Difficulty-Easy-green)

Problem: [191. Number of 1 Bits][problem]

[problem]: https://leetcode.com/problems/number-of-1-bits/description/


## How to solve

Simply read the least significant bit and shift the bits to the right.



## Complexities

The binary representation of the input number in the problem has a length of at most $32$.
For analysis, suppose that the input number is at most $O(N)$.

### Time

We visit each digit in the binary representation.
Thus, $O(\log N)$.
Note that the number $M$ has $\log_2 M$ digits in the binary representation.

### Space

Only $O(1)$ extra space required.
