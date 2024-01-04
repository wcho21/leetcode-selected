# README

- Problem: [344. Reverse String][problem]
- Difficulty: Easy

[problem]: https://leetcode.com/problems/reverse-string/description/



## How to solve

Just swap all characters.

Some languages have built-in reverse functions.
I could use them, but I didn't, because that's not what the problem asks I guess.



## Complexities

Suppose that the input string has a length of $N$.

### Time

The reversing visits each characters.
Thus, $O(N)$.

### Space

The problem requires not to use more than $O(1)$ extra space.
Of course, the input string takes $O(N)$ space.
