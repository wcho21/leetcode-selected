# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [316. Remove Duplicate Letters][problem]

[problem]: https://leetcode.com/problems/remove-duplicate-letters/description/


## How to solve

Think of the most lexicographically sooner character as an pivot point, and the input string is divided into two substring by the pivot point.
If all characters in the first part appear in the second part, we can discard all the characters in the first part.

Consider this example, `cbabc`.
We can think of the character `a` as a pivot point.
Since all characters in the first part `cb` appear also in the second part `bc`, we can discard the first part `cb`.
So, the answer is `abc`.

With this idea, we can come up a way to solve the problem.
The one of possible solution is as below.

First, mark the last occurrence index for each character, and create a set to store visited characters.
Then, as we read the input string, push each (not visited) character into a stack.

Whenever pushing the character, pop all characters which are not the last occurrence and are not in lexicographical order.
The popping step actually corresponds to "discarding first part" in the explanation above.
The discard character can appear later, and we have to push it to the stack.
So, set the discard charater as non-visited state.




## Complexities

Suppose that the input string has a length of $N$.

### Time

We visit each character $O(1)$ times. So, $O(N)$.

### Space

A hash table to mark the last occurrence stores $N$ indices.
A hash set to store the visited characters stores at most $N$ characters.
A stack stores at most $N$ characters.

All data structures used requires $O(N)$.
