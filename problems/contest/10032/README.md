# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [10032. Minimum Number of Operations to Make Array XOR Equal to K][problem]

[problem]: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/description/



## How to solve

XOR is [commutative][commutative], so we can defer XORs to make the number equal to `k`.
XOR all the elements first, then we do the deffered XORs to make the result equal to `k`.
The minimum number of XOR operations is just the number of different digits (in binary) between the `k` and all-element XOR result.

[commutative]: https://en.wikipedia.org/wiki/Commutative_property




## Complexities

Suppose that the list of input numbers has a length of $N$, and all the numbers including $K$ has at most $M$ digits.

### Time

The XOR operations occur $O(N)$ for the input numbers, and $O(M)$ to make the XOR result equal to `k`.
Thus, $O(N+M)$.

### Space

$O(1)$ extra space required.
