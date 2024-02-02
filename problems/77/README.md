# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [77. Combinations][problem]

[problem]: https://leetcode.com/problems/combinations/description/



## How to solve

The problem asks to find all combinations of $k$ numbers from the range $[1, n]$.

For example, let $k = 3$ and $n = 5$, and the combination have the form of $a_1, a_2, a_3$.
Note that the possible range for the first number $a_1$ is $[1, 3]$, for the second number $a_2$, $[a_1+1, 4]$, and for the third number $a_3$, $[a_2+1, 5]$.

In general, for arbitrary numbers $k$ and $n$, the range for the $i$-th number $a_i$ is $[a_{i-1}+1, n-k+1]$ where $a_0 = 0$.

Now we can construct each number of a combination.
One possible way is to choose each number $a_i$ in the range $[a_{i-1}+1, n-k+1]$, and recursively choose the next number $a_{i+1}$ in the range $[a_i+1, n-k'+1]$ where $k' = k-1$.



## Complexities

Suppose that the number $n$ is at most $N$.
Note that $k$ is also at most $N$.

### Time

The loop iterates exactly $n \choose k$ times.
Thus, $O({n \choose k})$.

### Space

An array to store all the combinations takes $O({n \choose k})$ space.
