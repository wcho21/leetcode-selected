# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [215. Kth Largest Element in an Array][problem]

[problem]: https://leetcode.com/problems/kth-largest-element-in-an-array/description/



## How to solve

We can solve this by simply sorting, but this problem asks to solve it without sorting.

First, we can keep $k$-th largest element using heap (`solution1`).

Second, we can find the $k$-th element with quickselect algorithm (`solution2`)



## Complexities

Suppose that the input list has $N$ elements.


### Time

`solution1`: the heap takes $O(\lg k)$ time to push each element.
Thus, $O(N \lg k)$ in total.

`solution2`: the quickselect algorithm takes $O(N)$ on average, and $O(N^2)$ in worst-case but with very low probability.



### Space

`solution1`: the heap takes $O(k)$ space.

`solution2`: only extra $O(1)$ space required.
