# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [77. Combinations][problem]

[problem]: https://leetcode.com/problems/combinations/description/



## How to solve

The problem asks to find all combinations of $k$ numbers from the range $[1, n]$.

For example, let $k = 2$ and $n = 4$.
Not that the possible range for the first number $a$ is $[1, 3]$.
Note that $3$ comes from $n - (k-1)$, which is $4 - 1$.
Choosing the second number is a subproblem to get combinations of $k-1$ numbers from the range $[a+1, 4]$.
Note that $4$ also comes from $n - (k-1)$.

Generally, for the problem $k$ and $n$ with the previous number $a$, the possible range is $[a+1, n-(k-1)]$.
We can solve this problem by recursion on $k$.



## Complexities

Suppose that the number $n$ is at most $N$.
Note that $k$ is also at most $N$.

### Time

The loop iterates exactly $n \choose k$ times.
Thus, $O({n \choose k})$.

### Space

An array to store all the combinations takes $O({n \choose k})$ space.
