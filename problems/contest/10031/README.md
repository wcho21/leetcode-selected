# README

![Difficulty Easy](https://img.shields.io/badge/Difficulty-Easy-green)

Problem: [10031. Smallest Missing Integer Greater Than Sequential Prefix Sum][problem]

[problem]: https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/description/



## How to solve

Get the sum for the sequential prefix, i.e., $n(j) = n(j-1)+1$ for $1 \leq j \leq i$.

If the sum is not in the input numbers, return it; otherwise, try the next number.
To quickly determine the sum is in the numbers, store the input number into a set first.



## Complexities

Support the list of the input numbers has a length of $N$.

### Time

All loops iterates $O(N)$ time.
Thus, $O(N)$.

### Space

To store the sequential prefix, $O(N)$ space required.
