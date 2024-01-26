# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [641. Design Circular Deque][problem]

[problem]: https://leetcode.com/problems/design-circular-deque/description/


## How to solve

The circular deque to create has a fixed size.
First, allocate one more cell than the given size.
We'll use this extra cell to determine whether the deque is empty or full.

Create two pointers.
One points the front cell to insert next at the front, and the other points the rear cell to delete next at the rear.
Move the front pointer for front operations, and likewise for rear pointer.

Whenever pointer goes out of the size, we do modular operation.
For example, if the front pointer is pointing the last cell and we're going to insert an element, reset the pointer to point the zeroth cell.



## Complexities

Suppose the circular deque has a size of $N$.

### Time

Initializing the deque may takes $O(N)$ time for allocating $N$ cells.

Obviously any operation takes $O(1)$ time.


### Space

The deque may takes $O(N)$ space.
