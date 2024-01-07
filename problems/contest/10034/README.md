# README

![Difficulty Hard](https://img.shields.io/badge/Difficulty-Hard-red)

Problem: [10034. Count the Number of Powerful Integers][problem]

[problem]: https://leetcode.com/problems/count-the-number-of-powerful-integers/description/


## How to solve

Steps:

- Get the number of powerful integers up to `finish`, and `start`.
- The difference is the answer.

The problem reduces to two main tasks.

- `count()`: Counting the number of powerful integers up to `n` (for given `n`)
- `lower`, `upper`: Determining the lower and upper bounds of the interval to count (using given `start` and `finish` in the problem)

By solving these, we can get the answer as `count(upper) - count(lower-1)`.


### Determining `lower` and `upper`

Suppose that, for example, the problem gives `start = 2345` and `suffix = 50`.
In this case, the powerful integers will be `2350`, `2450`, `2550`, and so on.

Now, for another example, let `suffix = 40`.
Then the powerful integers will start with `2440`, `2540`, etc.
We'll count the first two digits (such as `24`, `25`, ...).
Note that the starting number (`lower` bound) will be determined by `suffix`.
Specifically, if the remainder of `start / 100` is less than or equal to `suffix`, then we'll count the `start` for the answer. If not, we'll exclude it.

```
start: 2345
suffix:  50
lower: 23   (to include 2350)

start: 2345
suffix:  40
lower: 24   (to exclude 2340)
```

Similarly, we can determine the ending number (`upper` bound).

### Counting powerful integers

Now the problem reduces to a smaller problem to find `count(upper) - count(lower-1)`, where `count(n)` is a function that counts powerful integers from `0` to `n`.

Since the numbers that we'll count always have the same suffix, we're interested in the digits other than the suffix.
So we'll do not care the `suffix` value.
That is, here `n` is the digits other than `suffix` part.
For example, if `suffix = 34`, then we'll say `n = 12` for the number `1234`.

Suppose that `limit` is `6`.
How can we count powerful integers from `0` to `n`, if `n = 3456`?

For the leftmost (`1000`'s) digit, there are two cases.
If it is one of the numbers `0` to `2`, the rest digits can be any number between `0` and `limit (= 5)`.
Thus, `3*6*6*6` cases in total.
If it were `3`, the answer comes from the subproblem for `n = 456`.

The same process goes for the subproblem.
You'll find that, when you recursively solve this example by hand, some patterns appear as below.

```
n = 3456
    (0-2): 3*6*6*6
       3 : 4*6*6 + 5*6 + 7 (comes from count(456))

n = 456
    (0-3): 4*6*6
       4 : 5*6 + 7 (comes from count(56))

n = 56
    (0-4): 5*6
       5 : 7 (comes from count(6))

n = 6
    (0-6): 7

count(3456) = 3*6*6*6 + 4*6*6 + 5*6 + (6+1)
```

Therefore, if every digit is less than or equal to `limit`, the answer follows this pattern.
You can calculate this number by recursion or iteration.

What if one of digit is greater than `limit`?
Actually it gets easier to calculate in this case.

Consider `limit=2` and `n=3456`.
Then we can get immediately the answer by calculating `(limit+1)^4`, without leaving a subproblem.

Now only edge cases left.
For `count(0)`, we'll return `1`.
Note that the function `count(n)` counts the numbers up to `n`, so it includes the case when the number is `n<suffix>` (for example, when `suffix = 34` and `n = 2`, it counts three numbers `034`, `134`, and `234`) So we include the number `0<suffix>` for `count(0)`, which is the only case.

For similar reason, the call `count(-1)` returns `0` (nothing to count).
Note that we'll calculate `count(lower-1)`. If `lower = 0`, then `count(-1)` can be called.



## Complexities

Let `start` and `finish` number is at most $N$.

### Time

It iterates over the digits of numbers.
Since there are $\log_{10} N$ digits, it takes $O(\log N)$ time (assuming that calculating the power of a number is fast).

### Space

It requires an array of the number of the digits. Thus, $O(\log N)$.
