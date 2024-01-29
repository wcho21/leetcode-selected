# README

![Difficulty Easy](https://img.shields.io/badge/Difficulty-Easy-green)

Problem: [Array Partition][problem]

[problem]: https://leetcode.com/problems/array-partition/description/



## How to solve

Just take the numbers at odd indices from the sorted list of the input numbers.



## Complexities

Suppose that the list of input numbers has a length of $N$.

### Time

The whole time complexity depends on the time complexity for sorting, which we can assume takes $O(N \log N)$.


### Space

If sorting happens in-place, extra space required no more than $O(1)$.
