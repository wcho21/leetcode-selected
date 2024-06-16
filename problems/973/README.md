# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [973. K Closest Points to Origin][problem]

[problem]: https://leetcode.com/problems/k-closest-points-to-origin/description/



## How to solve

We can solve this as a sorting problem.

Simply sort by Euclidean distance and return $k$ smallest elements (`solution1`), or use max heap to keap $k$ smallest elements (`solution2`)




## Complexities

Suppose that the input list is of length $N$.

### Time

For `solution1`, the time complexity comes from the sorting algorithm (for example, $O(N\lg N)$ for merge sort).

For `solution2`, the heap requires $O(N \lg k)$ time to get $k$ smallest elements.

### Space

For `solution1`, the space complexity comes from the sorting algorithm.

For `solution2`, the heap requires $k$ space to keep $k$ smallest elements.
