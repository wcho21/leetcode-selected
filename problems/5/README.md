# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [5. Longest Palindromic Substring][problem]

[problem]: https://leetcode.com/problems/longest-palindromic-substring/description/



## How to solve

The input is not so large, so we can use a brute-force approach (see `solution1`) without time limit exceeded.

We can also use dynamic programming (see `solution2`).
Note that if `i` to `j` is palindrome, we can quickly determine whether `i-1` to `j+1` is also palindrome.

We may use a sliding window which moves from left to right, expanding its length whenever it matches a palindrome (see `solution3`).
Unlike dynamic programming, this method skips some non-longest palindromes.

Another method, called Manacher's algorithm, is faster one (see `solution4`).
When encoutering a palindrome, we can think of the current position (or index) as the center.
Then we can use results from previous indices, mirrored with respect to the center index.

Relative performances, i.e., elapsed time, are as follows:

| languages | solution1 | solution2 | solution3 | solution4 |
| :- | -: | -: | -: | -: |
| C++ | 1 | ~0.72 | ~0.098 | ~0.063 |
| Python | 1 | ~0.74 | ~0.10 | ~0.027 |
| TypeScript | 1 | ~1.6 | ~0.36 | ~0.28 |


## Complexities

Suppose that the string has a length of $N$.

### Time

#### Solution 1: brute force

Obviously, it iterates over $O(N^2)$ index pairs, and for each pair, it compares $O(N)$ characters.
Thus, $O(N^3)$.

#### Solution 2: dynamic programming

It iterates over the dynamic programming table, that is, $O(N^2)$ times.

#### Solution 3: sliding window

It scans palindrome for each index, and the scanning requires $O(N)$ time.
So, $O(N^2)$.

#### Solution 4: Manacher's algorithm

Consider a worst input `aaa...`.
The index access of outer loop takes $O(N)$, and the inner loop iterates at most two times.

Actually the time complexity of this algorithm is known as $O(N)$.

### Space

#### Solution 1: brute force

We need only loop variables.
So it takes $O(1)$ extra space.

#### Solution 2: dynamic programming

The table requires $O(N^2)$ space.

#### Solution 3: sliding window

Keeping two palindrome strings for comparison requires $O(N)$ space.
(If comparing indices instead of string, $O(1)$ extra space.)

#### Solution 4: Manacher's algorithm

To keep a radius for each index, we need $O(N)$ space.
