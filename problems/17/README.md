# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [17. Letter Combinations of a Phone Number][problem]

[problem]: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/



## How to solve

Just do exhaustive search using DFS (depth-first search).

Note that each DFS call keep track of two information, index for `digits` and currently combined letters `collected`.
When the search hits the end, that is, finds one of combinations, it collects the combination into the results `combs`.



## Complexities

Suppose that the input string has a length of $N$, and each digit is mapped to at most $M$ letters.

### Time

Think of a search tree, with branching factor $M$, and of height $N$.
Then, the number of the nodes is $O(M^N)$, which is the time complexity.

### Space

We recurse over $N$ digits, so the call stack depth is at most $O(N)$.

Since there are $O(M^N)$ combinations (see the time complexity analysis above), we need to store $O(M^N)$ strings into an array.

Thus, it takes $O(N + M^N) = O(M^N)$ space.
