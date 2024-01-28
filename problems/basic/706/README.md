# README

![Difficulty Easy](https://img.shields.io/badge/Difficulty-Easy-green)

Problem: [706. Design HashMap][problem]

[problem]: https://leetcode.com/problems/design-hashmap/description/


## How to solve

Just implement a hash table.
There are various ways to implement it, and here we use [chaining] to avoid collision.

[chaining]: https://en.wikipedia.org/w/index.php?title=Hash_table&oldid=1196850001#Separate_chaining



## Complexities

Suppose that there are $N$ element to put into the implmeneted hash table.

### Time

In average case, `put` and `get` methods require $O(1)$ time.
In worst case, they require $O(N)$ time.

### Space

The hash table takes $O(N)$ space.
