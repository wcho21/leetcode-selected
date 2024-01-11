# README

![Difficulty Easy](https://img.shields.io/badge/Difficulty-Easy-green)

Problem: [206. Reverse Linked List][problem]

[problem]: https://leetcode.com/problems/reverse-linked-list/description/


## How to solve

We can solve in a iterative manner (`solution1`).
Keeping the previous and current nodes, just change the `next` field of each node to have the previous one.

We can also solve in a recursive manner (`solution2`).

In each resursive call, change the `next` field of each node and return the result of the next recursive call, which returns the head of the reversed list in the end.
The base case is when the node in the function argument is empty.
In that case, return the previous node in the argument.


## Complexities

Suppose that the input linked list has a length of $N$.

### Time

In any solution, we visit each node $O(1)$ time.
Thus, $O(N)$.

### Space

In the iterative solution (`solution1`), we need only $O(1)$ extra space.

In the recursive solution (`solution2`), the call stack requires $O(N)$.
