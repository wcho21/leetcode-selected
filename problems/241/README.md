# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [241. Different Ways to Add Parentheses][problem]

[problem]: https://leetcode.com/problems/different-ways-to-add-parentheses/description/



## How to solve

Tokenize and evaluate (`solution1`).
First, tokenize the given expression into numbers and operators.
Then, recursively evaluate two divided sub-expressions, and join them into possible results.

If the language has a built-in evaluating function, we can use it (`solution2`).



## Complexities

Suppose that the input has $N$ operators.

### Time

This problems is one of applications of the Catalan number ($C_N$) pattern.
Since it recurses over all binary trees of $N$ nodes, it requires $C_N$ time.
Specifically, $C_N = O(4^n/n^{3/2})$.

### Space

Tokenization requires $O(N)$ spaces due to arrays to keep tokens (`solution1`).

If we use a built-in evaluating function, the space complexity comes from the function (`solution2`).
