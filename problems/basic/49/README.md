# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [49. Group Anagrams][problem]

[problem]: https://leetcode.com/problems/group-anagrams/description/



## How to solve

We need to group strings by a common property shared by those within the same anagram group.
Note that the strings in the same anagram group have the same occurrances for each character.

Here we're going to compare the sorted strings with each other to determine whether they belong to the same group, instead of counting occurrances of characters.
This will be done by using a hash table with the sorted string as a key and the original one as a value.
The values, i.e., the grouped strings, are the answer


## Complexities

Suppose that the input list of strings has a length of $N$, and each string has a length of at most $M$.

### Time

Assume that the sorting string takes $O(M \log M)$, then sorting all strings requires $O(NM \log M)$.

### Space

Extra $(NM)$ space requires due to a hash table used to store anagram groups.
