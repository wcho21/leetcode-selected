# README

![Difficulty Hard](https://img.shields.io/badge/Difficulty-Hard-red)

Problem: [23. Merge k Sorted Lists][problem]

[problem]: https://leetcode.com/problems/merge-k-sorted-lists/description/



## How to solve

We can solve using a priority queue, enqueuing and dequeuing all the values, like [heap sort][heapsort] (`solution1`).

[heapsort]: https://en.wikipedia.org/wiki/Heapsort

We can also solve in a divide-and-conquer manner (`solution2`).
In base case, we're given at most two lists. we can merge recursively in sorted order, or simply return the list if only one list given.
For more than two lists, reduce the lists into merged two lists using the base case.



## Complexities

Suppose that the number of lists is $N$, and each list has a length of at most $M$.

### Time

For `solution1`, the number of all elements is $O(NM)$, so enqueuing and dequeuing takes $O(NM \log NM)$.

For `solution2`, we visit each element $O(\log N)$ times to merge it into a single sorted list.
Thus, it requires $O(NM \log N)$.

### Space

For `solution1`, the priority queue takes $O(NM)$ cells.

For `solution2`, the call stack may require $O(NM)$ space.
