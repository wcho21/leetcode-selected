# README

![Difficulty Easy](https://img.shields.io/badge/Difficulty-Easy-green)

Problem: [349. Intersection of Two Arrays][problem]

[problem]: https://leetcode.com/problems/intersection-of-two-arrays/description/



## How to solve

Make a set for each two list of numbers, and iterate over one of sets to collect intersection.



## Complexities

Suppose that each list of numbers has a length of at most $N$.

### Time

Since it iterates over the lists of numbers, it takes $O(N)$ time.

### Space

Each set takes $O(N)$ space, and an array for intersection takes also $O(N)$ space.
Thus, $O(N)$ space required.
