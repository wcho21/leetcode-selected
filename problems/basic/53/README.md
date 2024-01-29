# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [53. Maximum Subarray][problem]

[problem]: https://leetcode.com/problems/maximum-subarray/description/


## How to solve

Suppose that the problem has been solved for `n-1` numbers.
We can solve the problem using [dynamic programming][dp] (`solution1`).
Using the maximum sum `sums[n-1]` from the case of `n-1`, we can determine the next maximum sum.
That is, we choose the greater number between the current number itself (`nums[n]`) and the sum the current number and the previous maximum sum (`sums[n-1] + nums[n]`).
Then the maximum number in the list of sums is the answer.

Here we can improve the space complexity (`solution2`), using the [Kadane's algorithm][kadane-alg].
Note that we only need to keep track of two numbers, which are the current sum `curSum` and the maximum sum `maxSum`.
Whenever the sum `curSum + nums[i]` is less than the current number `nums[i]`, update the current sum with the current number `nums[i]`.
Iterating through each number, we maintain the the greatest one as `maxSum`, which is the answer.

[kadane-alg]: https://en.wikipedia.org/w/index.php?title=Maximum_subarray_problem&oldid=1187835725#Kadane's_algorithm

We can solve in a divide-and-conquer manner (`solution3`), which the problem asks to do.
Assume that, for a list of numbers $a_1$ to $a_n$, we have the maximum sums for the first half, $a_1$ to $a_m$, and the second half, $a_m$ to $a_n$, where $m$ is the middle index and the intervals are right-open.
Calculate the "crossed sum", which is the maximum sum that contains the numbers $a_{m-1}$ and $a_m$.
Then choose the greatest one among the left sum, right sum and crossed sum.
The whole problem can be solved by solving the sub-problems recursively.



## Complexities

Suppose that the input list of numbers has a length of $N$.

### Time

For dynamic programming including Kadane's algorithm (`solution1` and `solution2`), we visit each number $O(1)$ times.
Thus, $O(N)$.

For the divide-and-conquer solution (`solution3`), we visit each number $O(\log N)$ times.
Thus, $O(N \log N)$.

### Space

For the simple dynamic programming (`solution1`), the array to store the maximum sums takes $O(N)$ space.

For the Kadane's algoritm (`solution2`), we use only $O(1)$ extra memory.

For the divide-and-conquer solution (`solution3`), each recursive call uses $O(1)$ extra memory, and the call stack depth is at most $O(\log N)$.
Thus, $O(\log N)$.
