# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [2. Add Two Numbers][problem]

[problem]: https://leetcode.com/problems/add-two-numbers/description/


## How to solve

Here we're going to solve the problem by adding the value in the shorter list to those in the longer list.
To do that, we'll assume the first one is longer.
If the second input list is actually longer, we can choose the second one as the first one by swapping.

Just update the nodes in the first list as the remainder of division by ten.
The quotient will be the carry.
If nonzero carry remains after visiting all nodes, then append a new node which has a value of the carry to the first list.



## Complexities

Suppose that the each input list has a length of at most $N$.

### Time

We visit each node $O(1)$ times.
Thus, $O(N)$.

### Space

Extra space required no more than $O(1)$.
