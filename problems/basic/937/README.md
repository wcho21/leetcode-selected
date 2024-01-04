# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [937. Reorder Data in Log Files][problem]

[problem]: https://leetcode.com/problems/reorder-data-in-log-files/description/



## How to solve

A sorting problem.
Just sort logs, by the order that the problem stated.

Note that we need to maintain the relative ordering for the "digit logs", and actually sort "letter logs" only.
If the sorting algorithm is [stable][stable], we can use the stability.

[stable]: https://en.wikipedia.org/w/index.php?title=Sorting_algorithm&oldid=1183276643#Stability

We're going to sort by keys.
We can imagine that the digit logs have their keys as a very large but the same value.
Then, the sorting algorithm will place all the digit logs after letter logs, but keep the relative ordering of digit logs.

If the language we're using lacks a built-in feature for keys, we can manually create a key function.
Since we don't want to calculate the same key more than once, we'll capture some store (i.e. hash table) for keys in the key function closure.

Now the sort function naturally sorts all the logs as we want.



## Complexities

Suppose that the input array of logs has a length of $N$, and each log string has a length of at most $M$.

### Time

For key calculation, finding the first space character spends $O(M)$ times for each $N$ log. Thus, $O(MN)$.

The whole time complexity depends on the sorting algorithm.
In most language, it takes $O(N \log N)$ time.
(Note that, in C++, $O(N (\log N)^2)$ time for `stable_sort()`.)

### Space

For in-place sorting, no extra space required.
If we need to keep the key store, $O(MN)$ space required.
