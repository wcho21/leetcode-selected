# README

![Difficulty Easy](https://img.shields.io/badge/Difficulty-Easy-green)

Problem: [21. Merge Two Sorted Lists][problem]

[problem]: https://leetcode.com/problems/merge-two-sorted-lists/description/



## How to solve

We can solve in a iterative manner (`solution1`).
Pick a node that has a smaller value and append it to a new linked list.

On the other hand, we can also solve in a recursive way (`solution2`).

Suppose each resursive call returns the head of merged list.
The base case is when the one of lists to merge has a empty head.
In that case, just return the head of the other list.
In recursive case, pick a node that has a smaller value, and to that node, append the merged list, which comes from the next recursive call.



## Complexities

Suppose that the each input list has a length of at most $N$.

### Time

In any solution, we visit each node $O(1)$ times.
Thus, $O(N)$.


### Space

In the iterative solution (`solution1`), we just need $O(1)$ extra space.

In the recursive solution (`solution2`), the call stack requires $O(N)$ space.
