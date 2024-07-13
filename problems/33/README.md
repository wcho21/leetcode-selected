# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [33. Search in Rotated Sorted Array][problem]

[problem]: https://leetcode.com/problems/search-in-rotated-sorted-array/description/



## How to solve

The problem is to find the index of the target number in the given list of $n$ numberes.
First, find the pivot index $p$.
Second, binary search with the pivot.
In this search, the half-open interval $[i, j)$ for the search means a virtual interval $[i+p, j+p \bmod n)$



## Complexities

Suppose the list of numbers has a length of $N$.

### Time

The pivot and the target number is found with binary search, so $\lg N$ time required.

### Space

Only $O(1)$ extra space required.
