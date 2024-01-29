# README

![Difficulty Easy](https://img.shields.io/badge/Difficulty-Easy-green)

Problem: [771. Jewels and Stones][problem]

[problem]: https://leetcode.com/problems/jewels-and-stones/description/


## How to solve

Just store the number of stones into an array, and get the number of jewels.

## Complexities

Suppose that the length of the input string (jewels and stones) has a length of at most $N$.

### Time

We visit each letter $O(1)$ times.
Thus, $O(N)$.

### Space

The array to store the number of stones takes $O(N) space.
