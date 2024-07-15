# README

![Difficulty Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Problem: [406. Queue Reconstruction by Height][problem]

[problem]: https://leetcode.com/problems/queue-reconstruction-by-height/description/



## How to solve

Use greedy approach with a max heap.

Each person is given by $h$ and $k$, where $h$ is the height and $k$ is the number of people in front who have a height $\geq h$.
Push each person into the heap so that the largest $h$ (and if the same $h$ then smallest $k$) pops out first.

Now, popping out each person as $h$ and $k$, insert the person at index $k$ in an array.
Then the array becomes the answer.

The correctness of the algorithm comes like this.
Suppose that the array contains $n$ people (as a partial answer).
For next person from the heap, there are two cases: (1) the same height with the previous person and (2) the smaller height.

In both case, the index $k$ is correct to insert the person into the array.
Note that all the heights of the people in the array is always greater than or equal to the current person, and $k$ becomes naturally the index since it is what the $k$ means.



## Complexities

Suppose that the input array has a length of $N$.

### Time

Initializing a heap and popping out all elements take $O(N \lg N)$ time.

For each element popped out, inserting an element into array may cause shifting the rest elements, that is, it takes time $O(N)$ in worst case.
In other words, since it takes $O(N)$ time for each element, $O(N^2)$ time required in total.

Therefore, the time complexity is $O(N^2)$.


### Space

A heap and an array takes $O(N)$ space.
