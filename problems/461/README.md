# README

![Difficulty Easy](https://img.shields.io/badge/Difficulty-Easy-green)

Problem: [461. Hamming Distance][problem]

[problem]: https://leetcode.com/problems/hamming-distance/description/



## How to solve

We have to count the number of different corresponding bits for two numbers.

Do an XOR operation with the given two numbers.
Then the number of one bits in the result is the answer.
Note that an XOR operation yields one bits where the corresponding bits are different.



## Complexities

Suppose that the two input numbers are at most $N$.

### Time

Since we visit each digit in the binary representation of the two numbers, $O(\log N)$ time required.
Note that the number $M$ has $\log_2 M$ digits in the binary representation.

### Space

Only $O(1)$ extra space required.
