# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [347. Top K Frequent Elements][problem]

[problem]: https://leetcode.com/problems/top-k-frequent-elements/description/



## How to solve

We can solve the problem using a priority queue or sorting, and in Python there is an one-liner solution.
```
return list(map(lambda x: x[0], Counter(nums).most_common(k)))
```

However, since the problem asks to solve with time complexity better than $O(N \log N$), we'll use some steps in the [bucket sort][bucket-sort].

[bucket-sort]: https://en.wikipedia.org/wiki/Bucket_sort

Suppose that we're asked to get the top `k` frequent numbers.
First, count the number of occurrences (that is, frequency) for each input number.
Then for each count, create a bucket, which contains the numbers that correspond to that count.
Now, collect `k` numbers from the buckets, checking the buckets in the decreasing order of count.



## Complexities

Suppose that the number array has a length of $N$.
Note that the input number `k` is at most $N$.

### Time

We visit each number $O(1)$ times.
Thus, $O(N)$.

### Space

The array to store the counts and the buckets may take $O(N)$ space.
