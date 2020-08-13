# Sudoku-Solver
## Summary
This is an older project that I worked on in school at Michigan State. We were tasked with making code that can solve a sudoku board. The standard sudoku board is 9x9 and has some given values and some blank values. The way the board is formatted is that each row is a list of 9 elements from top to bottom where each blank is given a value of zero. So an example of a board would be 
```python
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
```
## Strategy
The code will iterate through the values that are 0 and brute force try putting in 1-9 for the zero and unless that number is already in the row column or box. Once it finds a value that fits, it will replace the zero with the correct value and move on along the row until there are no zero values left.