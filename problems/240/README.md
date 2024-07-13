# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [240. Search a 2D Matrix II][problem]

[problem]: https://leetcode.com/problems/search-a-2d-matrix-ii/description/



## How to solve

Beginning at the bottom left corner, move a pointer if the number is not the given target.



## Complexities

Suppose the matrix has a width of $M$ and a height of $N$.

### Time

Since it iterates over at most $M+N-1$ numbers, it takes $O(M+N)$ time.

### Space

Only $O(1)$ extra space required.
