# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [46. Permutations][problem]

[problem]: https://leetcode.com/problems/permutations/description/



## How to solve

### DFS (Depth-first search)

Just do exhaustive search using DFS (depth-first search) (`solution1`).

Think of the search tree.
If we've chosen some numbers, the remained numbers represent the neighbor nodes.

### Swapping and recursion

We can solve the problem by swapping numbers and recursion (`solution2`), and we don't need the extra memory to remember which number is visited as in `solution1`.

For each recursion, we determine the last number of a permutation by (or not by) swapping input numbers.
After that, the problem with $n$ input numbers reduces to the subproblem with $n-1$ input numbers.

### Heap's algorithm

We can optimize the second solution, which is known as Heap's algorithm (`solution3`).
This version reduces the number of swapping to half.



## Complexities

Suppose that there are $N$ input numbers.

### Time

For DFS (`solution1`), we visit each number to choose the next number to construct a permutation.
That is, it takes $O(N)$ time for $N$-th number in a permutation.
Thus, $O(N^N)$.

For swapping and recursion (`solution2`), we visit $N-i+1$ numbers to choose $i$-th number of a permutation.
Thus, the time complexity is $O(N \times (N-1) \times \dots \times 1)$, which is $O(N!)$.
Note that we need to swap two times for each iteration.

In Heap's algorithm (`solution3`), we need to swap once for each iteration.
The complexity is still $O(N!)$.

### Space

In any solution, the call stack may take $O(N)$ space and the list of all permutations takes $O(N!)$.
So, $O(N!)$.
