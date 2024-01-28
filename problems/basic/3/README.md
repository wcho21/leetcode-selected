# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [3. Longest Substring Without Repeating Characters][problem]

[problem]: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/



## How to solve

Basically we can use sliding window technique, which moves two pointers.
Specifically, move the right pointer if the window contains no repeating characters, and update the longest length.
If it contains a repeating charater, move the left pointer to exclude the character from the window.

When moving the left pointer, we can use a hash table as an optimization.
That is, not moving the pointer one by one, but moving it to the next character just after the last occurrence of the repeating character.
To do that, we can keep the last occurrences using a hash table.



## Complexities

Suppose that the length of the input string has a length of $N$.

### Time

We visit each character $O(1)$ times.
Thus, $O(N)$.

### Space

The hash table that stores the last occurrences may take $O(N)$ space.
