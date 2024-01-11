# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [92. Reverse Linked List II][problem]

[problem]: https://leetcode.com/problems/reverse-linked-list-ii/description/


## How to solve

Keep the nodes just before and after the interval to reverse.
For example, if the problem asks to reverse a list from the third to seventh node, keep the second and eighth nodes.
Then, after reversing the list, append the seventh node to the reversed list, and again append the list to the second node.



## Complexities

Suppose that the input linked list has a length of $N$.

### Time

We visit each node $O(1)$ times.
Thus, $O(N)$.

### Space

Extra space required no more than $O(1)$.
