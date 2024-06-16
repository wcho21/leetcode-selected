# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [179. Largest Number][problem]

[problem]: https://leetcode.com/problems/largest-number/description/


## How to solve

Solve as a sorting problem, with a custom comparator.
The comparator compares two strings that extended to the sum of their lengths.
For example, to compare "3" and "30", extend them as "33" and "30".
For another example, "880" and "8803" will be compared as "8808803" and "8803880".



## Complexities

Suppose that the input list has a length of $N$.

### Time

Time complexity comes from the sorting algorithm.

Note that each time of comparison, it visits every digits in two extended strings.
We can bound the number of visits as $\leq 2L$ or $O(L)$ where $L$ is the length of the longest string.
Therefore, if the sorting algorithm compares $M$ times, the time complexity is $O(LM)$.
For example, the merge sort gives $O(MN \lg N)$.


### Space

Space complexity comes from the sorting algorithm.
