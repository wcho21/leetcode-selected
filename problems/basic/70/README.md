# README

![Difficulty Easy](https://img.shields.io/badge/Difficulty-Easy-green)

Problem: [70. Climbing Stairs][problem]

[problem]: https://leetcode.com/problems/climbing-stairs/description/



## How to solve

We can think of this problem as a Fibonacci number problem.
Simply calculate a Fibonacci number using [dynamic programming][dp].

[dp]: https://en.wikipedia.org/wiki/Dynamic_programming



## Complexities

Suppose that the input number is $N$.

### Time

Since we calculate each Fibonacci number up to $N$, it takes $O(N)$ time.

### Space

An array to store the Fibonacci numbers take $O(N)$ space.
