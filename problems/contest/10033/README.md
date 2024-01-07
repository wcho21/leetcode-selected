# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [10033. Minimum Number of Operations to Make X and Y Equal][problem]

[problem]: https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/description/



## How to solve

We can think of this problem as a task to find the minimum distance in a graph, so we can simply use BFS.



## Complexities

Suppose that the input numbers $x$ and $y$ are given at most $N$.

### Time

The BFS visits up to about $2N$ nodes.
For simplicity, consider only incrementing and decrementing operations with $x = N$ and $y = 1$.
Then, until $x$ reaches to $y = 1$, there will be $N-1$ operations for incrementing and decrementing operations.
Since in the actual problem we also have dividing operations, $x$ reaches to $y=1$ faster.
Therefore, we can safely conclude that the BFS takes $O(N)$ time.

### Space

Since the BFS takes $O(N)$ time, we need to store which nodes the BFS has visited for up to $O(N)$ nodes.
The BFS queue also requires $O(N)$ time.
Thus, $O(N)$.
