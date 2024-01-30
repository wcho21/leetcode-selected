# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [200. Number of Islands][problem]

[problem]: https://leetcode.com/problems/number-of-islands/description/



## How to solve

It asks the number of [connected components][wp-cc].

[wp-cc]: https://en.wikipedia.org/w/index.php?title=Component_(graph_theory)&oldid=1195075929

Simply using DFS (depth-first search), fill each island with water.
The number of DFS called is be the answer.



## Complexities

Suppose that the input grid has $N$ rows and $M$ columns.


### Time

We visit each cell $O(1)$ times, and there are $NM$ cells in the grid.
Note that there are at most 4 neighbors for each cell, so retrieving neighbors takes $O(1)$ time.
Thus, $O(MN)$.


### Space

Note that the longest path will be diagonal and have the length of $O(N+M)$.
The size of additional space, that is, the call stack depth will also be at most $O(N+M)$.
