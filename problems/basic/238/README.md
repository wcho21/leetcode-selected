# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [238. Product of Array Except Self][problem]

[problem]: https://leetcode.com/problems/product-of-array-except-self/description/



## How to solve

The problem requires not to use the division operation.

We can just get the product for each number except that number, but it's infeasible to solve in a brute force manner.
So we pre-calculate products partially, and for each number, just use the precalculated products.

Specifically, for each number, we can calculate the two products, which we'll call a "prefix product" and a "suffix product".
The "prefix" one is from the first number to the just previous number, and the "suffix" one from the next number to the last number.



## Complexities

Suppose that the list of numbers has a length of $N$.

### Time

It visits each number O(1) times. So, $O(N)$.

### Space

To store precalculated numbers, we need $O(N)$ space
