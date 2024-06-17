# README

![Difficulty Easy](https://img.shields.io/badge/Difficulty-Easy-green)

Problem: [169. Majority Element][problem]

[problem]: https://leetcode.com/problems/majority-element/description/


## How to solve

There are various ways to solve this problem.

First, simply sort and choose the middle element (`solution1`).
This is correct since the majority element is assumed to exist.

Second, divide and conquer like merge sort. (`solution2`)
From two solutions for divided sub arrays, choose the first one if it is the majority element.
This is also correct since at least one sub array have the majority element.

Third, Boyer-Moore voting algorithm. (`solution3`)
Assume an element is the majority element until other elements are encountered more than the assumed one.
The correctness of this algorithm assume that there is the majority element.



## Complexities

Suppose that the list of input numbers has a length of $N$.

### Time

The time complexity of the first method (`solution1`) comes from the sorting algorithm.

The second method (`solution2`) requires $O(N \lg N)$ time like merge sort.

The third one (`solution3`) requires $O(N)$ time.

### Space

For the first method, the space complexity comes from the sorting algorithm.

For the other methods, they require $O(1)$ extra space.
