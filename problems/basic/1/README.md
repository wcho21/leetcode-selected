# README

![Difficulty Easy](https://img.shields.io/badge/Difficulty-Easy-green)

Problem: [1. Two Sum][problem]

[problem]: https://leetcode.com/problems/two-sum/description/


## How to solve

The input number is not large, so the problem is feasible to solve in a brute force manner (see `solution1`).

However, we can solve the problem by visiting each number only once (see `solution2`).
For each number `num`, we can keep the index as value and the `target-num` as key.
Then we can find the index when we encounter a number, `target-num`, that adds up to `target` with that `num`.



## Complexities

Suppose that the list of input numbers has a length of $N$.

### Time

For the brute force method (`solution1`), it takes $O(N^2)$, since it uses a nested loop over $N$.

For the one-pass method (`solution2`), it takes $O(N)$, because it visits each number only once.

### Space

For the brute force method (`solution1`), no extra space required other than the loop variables.
So, $O(1)$.

For the one-pass method (`solution2`), it requires a hash table that takes $O(N)$.
