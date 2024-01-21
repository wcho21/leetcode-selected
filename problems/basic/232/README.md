# README

![Difficulty Easy](https://img.shields.io/badge/Difficulty-Easy-green)

Problem: [232. Implement Queue using Stacks][problem]

[problem]: https://leetcode.com/problems/implement-queue-using-stacks/description/


## How to solve

Create two stacks, which we'll call the first and second stack.

For `push` method of queue, just push element onto the first stack.

For `pop` and `peek` methods of queue, pop and peek from the second stack.
If the second stack is empty, pop all elements from the first stack and push them onto the second stack, before doing actual pop and peek.


## Complexities

Suppose that the number of operations (such as push and pop) is $N$.


### Time

Clearly, the `push` method requires $O(1)$ time.

For the `pop` and `peek` methods, note that we visit each pushed element at most twice.
The first time is when moving from the first to the second stack, and the second time is when popping it from the second stack.
Thus, amortized $O(1)$.


### Space

In worst case, all operations can be `push`.
So, the queue requires $O(N)$ space.
