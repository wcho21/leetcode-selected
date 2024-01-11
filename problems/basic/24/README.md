# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [24. Swap Nodes in Pairs][problem]

[problem]: https://leetcode.com/problems/swap-nodes-in-pairs/description/


## How to solve

What the problem asks to do is straightforward and clear.
We can solve in an iteratively manner (`solution1`), or a recursive manner (`solution2`).
In either method, change `next` fields for each pair of nodes.



## Complexities

Suppose that the input linked list has a length of $N$.

### Time

In either solution, we visit each node $O(1)$ times.
Thus, $O(N)$.


### Space

In the iterative method (`solution1`), extra space required no more than $O(1)$.

In the recursive method (`solution2`), the call stack requires $O(N)$.
