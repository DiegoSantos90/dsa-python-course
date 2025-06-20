'''
1020. Number of Enclaves
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
A move consists of walking from one land cell to another adjacent (4-directionally)
land cell or walking off the boundary of the grid.
Return the number of land cells in grid for which we cannot walk
off the boundary of the grid in any number of moves.

Example 1:
Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

Example 2:
Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.


Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.

Time Complexity: O(m * n)  # Each cell is visited once
Space Complexity: O(m * n)  # Space for the visited set
'''
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if not grid:
            return 0

        def dfs(r, c):
            if ((r, c) in visited_cells or
                    r < 0 or c < 0 or
                    not grid[r][c]):
                return 0

            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            visited_cells.add((r, c))
            res = 1

            for dr, dc in directions:
                res += dfs(r + dr, c + dc)
            return res

        land, borderLand = 0, 0
        visited_cells = set()

        for r in range(ROWS):
            for c in range(COLS):
                land += grid[r][c]
                if (grid[r][c] == 1 and (r,c) not in visited_cells and
                        (c in [0, COLS -1] or r in [0, ROWS - 1])):
                    borderLand += dfs(r,c)

        return land - borderLand