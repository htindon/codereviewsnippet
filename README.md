# Code Review Example: Palindrome Check

## Problem Description
The task was to write a function to check if a string is a palindrome. A palindrome is a word that reads the same backward as forward, ignoring spaces and case.

## Code Issues in `palindrome_before.py`
- The original code used string slicing (`s[::-1]`) to reverse the string, which creates a new string and uses extra memory.
- It is not optimized for large strings, as it requires additional memory.

## Improvements in `palindrome_after.py`
- The optimized version uses two pointers to compare characters from both ends of the string, reducing space complexity to O(1).
- The code returns `False` as soon as a mismatch is found, making it more efficient in terms of time complexity.
