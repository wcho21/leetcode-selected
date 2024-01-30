# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [17. Letter Combinations of a Phone Number][problem]

[problem]: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/



## How to solve

We'll solve in a recursive way.
The base case is when there is no letters left to make combination, and we return the empty string.
Now assume that we're given a string $a_1 a_2 \dots a_N$ of length $N$, and we've solved the problem for $a_{i+1} \dots a_N$.
Since we have the combinations for the substring $a_{i+1} \dots a_N$, simply prepend letters to all the combinations and return the results.



## Complexities

Suppose that the input string has a length of $N$, and each digit maps to at most $M$ letters.

### Time

For each character, we iterate over the combinations, and for each combination, iterate over each mapped letter.

Note that for $i$-th character, since there are $O(M^(N-i))$ combinations to iterate over, the whole loop has $O(M^(N-i+1))$ iterations due to the mapped letters.
So the whole time complexity becomes a geometric sum $M + M^2 + \dots M^N$, which is $O(M^N)$.

### Space

We call a recursive function for each character, so the call stack depth is $O(N)$.

There are $O(M^N)$ combinations (see above time complexity analysis), an array to store all the combinations have $O(M^N)$ strings.
Each combination is a string of a length of $N$.
Thus, the array takes $O(NM^N)$ space.
