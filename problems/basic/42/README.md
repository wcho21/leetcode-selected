# README

![Difficulty Hard](https://img.shields.io/badge/Difficulty-Hard-red)

Problem: [42. Trapping Rain Water][problem]

[problem]: https://leetcode.com/problems/trapping-rain-water/description/


## How to solve

First, find where is the maximum height.
From the left to the maximum height, we scan each height and get the amount of trapped water.
Specifically, starting from the leftmost height, we keep the maximum height that we've encountered so far.
The trapped water is then `(maximum height so far) - (current height)`.

Do the same for the rest but in the opposite direction, that is, starting from the rightmost height to the maximum height.
Sum them up.
This is the answer.

## Complexities

Suppose that the list of heights has a length of $N$

### Time

We visits each height.
Thus, $O(N)$.

### Space

Only $O(1)$ extra space required.
