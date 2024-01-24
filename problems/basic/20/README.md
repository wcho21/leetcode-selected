# README

![Difficulty Easy](https://img.shields.io/badge/Difficulty-Easy-green)

Problem: [20. Valid Parentheses][problem]

[problem]: https://leetcode.com/problems/valid-parentheses/description/


## How to solve

The solution is simple.
First, create a stack.
Whenever an opening parenthesis encountered, push it onto the stack.
For a closing parenthesis, pop an opening parenthesis from the stack and compare it with the current closing one.
By doing this, we can determine if the input is valid or not.

There are two edge cases to cover.
The first one is stack underflow, that is, when the stack is empty when a closing parenthesis encountered.
This case means that there is an unmatched closing parenthesis.
The other one is when stack is not empty after reading the input string.
This means that an unmatched opening parenthesis remains in the stack.
Both cases indicate that the input is not valid.



## Complexities

Suppose that the input string has a length of $N$.

### Time

We visit each character $O(1)$ times.
Thus, $O(N)$.

### Space

Because of the stack, $O(N)$ space required.
