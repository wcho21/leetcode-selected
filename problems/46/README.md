# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [46. Permutations][problem]

[problem]: https://leetcode.com/problems/permutations/description/



## How to solve

### DFS (Depth-first search)

We can think of the problem as a graph problem (`solution1`).
Specifically, the input numbers can be viewed as a graph where each number has every number as neighbors, including itself.
Using DFS, we can find all permutations.

### Swapping and recursion

We can solve the problem by swapping numbers and recursion (`solution2`).

Assume that, we've chosen the first $N-1$ numbers of a permutation, and swapped numbers to put them in the first $N-1$ places.
That is, we've constructed an initial part of a permutation, and we'll not care about the numbers in it.

Now choose $N$-th number among the remaining numbers, which have not yet been chosen, and put the number in $N$-th place by swapping.
Whenever we've chosen all numbers, the list of swapped numbers is one of possible permutations.

### Heap's algorithm

Based on the second solution, there is an optimized version, known as Heap's algorithm (`solution3`).
Using this algorithm, we can reduce the number of swapping by half.



## Complexities

Suppose that there are $N$ input numbers.

### Time

For DFS (`solution1`), we visit each number to choose the next number to construct a permutation.
That is, it takes $O(N)$ time for $N$-th number in a permutation.
Thus, $O(N^N)$.

For swapping and recursion (`solution2`), we visit $N-i+1$ numbers to choose $i$-th number of a permutation.
Thus, the time complexity is $O(N \times (N-1) \times \dots \times 1)$, which is $O(N!)$.

Note that we swap numbers two times for each iteration.
The first time to make a permutation, and the second time to recover the original.
In Heap's algorithm (`solution3`), just a single swapping occurs for each iteration, the complexity remains $O(N!)$ though.

### Space

In any solution, the call stack may take $O(N)$ space and the list of all permutations takes $O(N!)$.
So, $O(N!)$.
