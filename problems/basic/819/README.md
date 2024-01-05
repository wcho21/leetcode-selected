# README

![Difficulty Easy](https://img.shields.io/badge/Difficulty-Easy-green)

Problem: [819. Most Common Word][problem]

[problem]: https://leetcode.com/problems/most-common-word/description/



## How to solve

This is a string-handling problem.
The task is to find the most common word, but before doing that, some preprocessing is required.
Specifically, we need to remove non-alphabetic characters, and convert all alphabets to lowercase.
In this step, we may use regular expression to search all alphabet words.

We can use a hash table to count occurences for each word, and a hash set to quickly figure out that a word is banned.
The word that has the greatest number of occurrences is the answer.



## Complexities

Suppose that the input paragraph has a length of $N$, and the list of banned words has a length of $M$.

### Time

Assume that matching using regular expressions takes $O(N)$ time.

There can be $O(N)$ words in the input paragraph.
So, it takes $O(N)$ time to find the maximum by manually counting occurences for each word.

In worst case, we'll find that top $M$ words are banned, so $M+1$-th word is the most common word.
Thus, the whole time complexity is $O(N+M)$.

### Space

A list to store words and a hash table to count occurrences take $O(N)$ space.
A hash set for banned words takes $O(M)$ space.
Thus, $O(N+M)$ space required.
