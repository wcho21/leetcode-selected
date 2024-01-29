# README

![Difficulty Easy](https://img.shields.io/badge/Difficulty-Easy-green)

Problem: [225. Implement Stack using Queues][problem]

[problem]: https://leetcode.com/problems/implement-stack-using-queues/description/



## How to solve

Whene push an element to the stack, actually enqueue the element.
To dequeue the element first, dequeue the rest element and enqueue again.
Now the rest operations are obvious to implement.



## Complexities

Suppose that the number of operations is $N$.

### Time

Note that the push operation requires $O(N)$ time, since it dequeues and enqueues the elements it contains.
The rest opreations requires $O(1)$ times.

### Space

In worst case, there can be $N$ push operations.
Thus, the stack takes $O(N)$ space.
