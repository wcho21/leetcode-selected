# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [15. 3Sum][problem]

[problem]: https://leetcode.com/problems/3sum/description/


## How to solve

The upper limits of the input numbers is 3000.
Note that it is infeasible to solve this problem in a brute force manner becuase there are $> 10^9$ cases to iterate through.

Sort the list of numbers first, in increasing order.
Now the repeat the following steps.

1. Choose the least number, that is, the leftmost number in the list.
    (For the next iteration, exclude the same numbers as this number from the list.)
1. For the remaining numbers, use two pointer technique to find two numbers that add up to the negative of the least number, so that the three numbers add up to zero.
1. Whenever finding such two numbers, skip the same numbers in the list.



## Complexities

Suppose that the list of numbers has a length of $N$.

### Time

Assume that sorting takes $O(N \log N)$.

It finds two numbers, which takes $O(N)$ time, for $O(N)$ least numbers.

Thus, $O(N^2)$.

### Space

If sorting is an in-place algorithm, extra space required no more than $O(1)$.
