# README

![Difficulty Easy](https://img.shields.io/badge/Difficulty-Easy-green)

Problem: [234. Palindrome Linked List][problem]

[problem]: https://leetcode.com/problems/palindrome-linked-list/description/



## How to solve

First, a straightforward solution is just converting the input linked list into an array, and checking if it's palindrome using random access (`solution1`).

Another solution is using a "runner" technique (`solution2`).
Place runners in the middle of the linked list, and compare the values by having the runners iterate over nodes from the middle to the both ends.

To place a runner in the middle, we prepare "slow" and "fast" runners.
The fast one runs at double speed of the slow one, so when the fast one reaches the end, the slow one remains in the middle.



## Complexities

Suppose the input linked list has a length of $N$.

### Time

In any solution, we visit each node $O(1)$ times.
Thus, $O(N)$.

### Space

In `solution1`, the converted array requires $O(N)$ space.

In `solution2`, we need $O(1)$ extra space.
