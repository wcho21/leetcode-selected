# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [622. Design Circular Queue][problem]

[problem]: https://leetcode.com/problems/design-circular-queue/description/



## How to solve

Allocate an array whose capacity is `size+1` for the given size.

Create two pointers.
The `push` pointer points a cell to push next, the `pop` pointer to pop next.

When two points point the same cell, the queue is empty.
When the next cell of `push` is where `pop` points, the queue is full.
Note that we allocated one more extra cell than the given size, and we use the extra cell to detect whether the queue is empty or full.



## Complexities

Note that the size of the circular queue is $N$.

### Time

The enqueuing and dequeuing requires $O(1)$ time.
Checking the queue is full or empty also requires $O(1)$ time.

### Space

The circular queue takes at most $N$ cells.
Thus, $O(N)$.
