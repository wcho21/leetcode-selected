# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [739. Daily Temperatures][problem]

[problem]: https://leetcode.com/problems/daily-temperatures/description/


## How to solve

Create an array to store the number of days to wait.

Then, iterate over indices of the input temperature array.
Note that we can treat the index as a day number.

Push each day number onto a stack.
We can get the temperatures on the current day (using the current index) and the past day (using the top element of the stack).
Whenever the temperatur of the current day is greater than the one of the past day, pop the past day from the stack and get the day difference.
The day difference is the number of days to wait to get a warmer temperature.



## Complexities

Suppose that the input temperature array has a length of $N$.

### Time

We visit each temperature $O(1)$ times.
Thus, $O(N)$.

### Space

The output array (the numbers of days to wait) and the stack takes $O(N)$ space.
