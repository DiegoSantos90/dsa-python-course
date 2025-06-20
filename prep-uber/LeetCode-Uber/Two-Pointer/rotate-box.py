'''
1861. Rotating the Box
Attempted
Medium
Topics
conpanies icon
Companies
Hint
You are given an m x n matrix of characters boxGrid representing a side-view of a box. Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in boxGrid rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.

 

Example 1:



Input: boxGrid = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]
Example 2:



Input: boxGrid = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]
Example 3:



Input: boxGrid = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]
 

Constraints:

m == boxGrid.length
n == boxGrid[i].length
1 <= m, n <= 500
boxGrid[i][j] is either '#', '*', or '.'.
'''

'''
Basically we need to transform a line into column considering the following
1 - Stone falls down until lands in a obstacle (*), another stone (#) or bottom of the box
2 - Obstacles doesnt affect by gravity
3 - Inertia from box does not affect stones in horizontal positions

Input = [['#', '.'], ['.', '#']]
Output = [['.', '.'
          ['#'] '#']

Time Complexity: O(m * n)  # Each cell in the matrix is visited once
Space Complexity: O(1)  # No additional space used for the output, we modify the input in place
'''
from typing import List

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        ROWS, COLS = len(boxGrid), len(boxGrid[0])


        for r in range(ROWS):
            i = COLS - 1
            for c in reversed(range(COLS)):
            #for c in range(COLS - 1, -1, -1):
                if boxGrid[r][c] == "#":
                    boxGrid[r][c], boxGrid[r][i] = boxGrid[r][i], boxGrid[r][c]
                    i -= 1
                elif boxGrid[r][c] == "*":
                    i = c - 1

        print(f"Transformed boxGrid: {boxGrid}")
        # Create an empty list to store the transposed result
        res = []

        for c in range(COLS):
            col = []
            for r in range(ROWS):
                col.append(boxGrid[r][c])
            res.append(col)

        return res
    
    # ...existing code...

    def print_box(self, matrix, title=""):
        print(f"\n{title}")
        print("-" * (len(matrix[0]) * 2 + 3))
        for row in matrix:
            print("|", end=" ")
            for cell in row:
                print(cell, end=" ")
            print("|")
        print("-" * (len(matrix[0]) * 2 + 3))

if __name__ == "__main__":
    solution = Solution()

    boxGridTest1 = [["#",".","*","."],["#","#","*","."]]
    solution.print_box(boxGridTest1, "Original Box:")
    result = solution.rotateTheBox(boxGridTest1)
    solution.print_box(result, "Rotated Box:")

    boxGridTest2 = [["#", ".", "#"]]
    solution.print_box(boxGridTest2, "Original Box:")
    result = solution.rotateTheBox(boxGridTest2)
    solution.print_box(result, "Rotated Box:")

    boxGridTest3 = [["#",".","*","."],["#","#","*","."]]
    solution.print_box(boxGridTest3, "Original Box:")
    result = solution.rotateTheBox(boxGridTest3)
    solution.print_box(result, "Rotated Box:")
