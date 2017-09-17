# Cyclic Rotation (part deux)

An array A consisting of N items is given.
An offset O and a length L is also given.

Swap the order of the L items at offset O in array A.

For example, A = [3, 8, 9, 7, 6], O = 1, and L = 3, yields [3, 7, 9, 8, 6].

Write a function: `function solution( A, O, L )` that returns a new array.

Assume that:
* O >= 0
* L should be <= N
* O + L should be <= N

Extra credit:
* Determine what to do if L > N
* Determine how to swap the values around the edge of the array
	* A = [3, 8, 9, 7, 6], O = 3, L = 3 should yield [7, 8, 9, 3, 6]

