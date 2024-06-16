# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [56. Merge Intervals][problem]

[problem]: https://leetcode.com/problems/merge-intervals/description/


## How to solve

Sort intervals in the order of its beginning and then end.
Make a stack, and iterate over the sorted intervals.
If the beginning of interval is greater than the end of the last interval in the stack, push it into the stack.
Otherwise, update the end of the last interval to be the greater one.



## Complexities

Suppose that the input list has a length of $N$.

The time and space complexity comes from the sorting algorithm.
