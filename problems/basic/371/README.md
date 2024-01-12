# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [371. Sum of Two Integers][problem]

[problem]: https://leetcode.com/problems/sum-of-two-integers/description/



## How to solve

Simulate an [adder][adder] with only bit operations.

[adder]: https://en.wikipedia.org/wiki/Adder_(electronics)

Suppose we add two numbers `a` and `b`.
For each bit position, we can calculate carries (`carry`) by `(a & b << 1)`.
Then we can add the remaining bits by `(a ^ b)`, which we'll call `added`.
Note that we excluded the bits that have already considered when calculating `carry`.

Now set the `carry` and `added` to be `a` and `b`, and repeat the steps above.
The `added` is the answer when the `carry` is zero.

See an example below for `6+7`.

```text
a    : 0110 (6)
b    : 0111 (7)
-----------
a&b  : 0110
carry: 1100
added: 0001

a    : 1100
b    : 0001
-----------
a&b  : 0000
carry: 0000
added: 1101 (13)
```



## Complexities

Suppose that the input numbers are at most $N$.
Note that the binary representations of the numbers have a length of at most $O(\log N)$.


### Time

In the worst case, we repeat the steps up to $O(\log N)$ times.
Consider the case when `a = 1111` and b = 0001` in binary representation.
The carry is shifted to the left for each step, and will be zero in $O\log N)$ times due to overflow.

### Space

Only $O(1)$ extra space required.
