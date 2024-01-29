# README

![Difficulty Easy](https://img.shields.io/badge/Difficulty-Easy-green)

Problem: [125. Valid Palindrome][problem]

[problem]: https://leetcode.com/problems/valid-palindrome/description/


## How to solve

First, filter out all characters that we're not interested in, that is, not alphabets or numbers.

For alphabet comparison, convert all alphabets to lowercase.

Finally, check if the string is palindrome, by comparing it with the reversed one, or manually comparing each pair of characters using index operations.



## Complexities

Suppose that the input string has a length of $N$.

### Time

The filtering visits each characters, and so does checking palindrome. Thus, $O(N)$.

### Space

The filtered string requires $O(N)$ space.
