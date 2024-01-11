# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [328. Odd Even Linked List][problem]

[problem]: https://leetcode.com/problems/odd-even-linked-list/description/


## How to solve

Just make two new lists for odd-index nodes and even-index nodes, and append the latter to the former.



## Complexities

Suppose that the input linked list has a length of $N$.

### Time

We visit each node $O(1)$ times.
Thus, $O(N)$.

### Space

Extra space required no more than $O(1)$.
