'''
200. Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

Time Complexity: O(m * n)  # Each cell is visited once
Space Complexity: O(m * n)  # Space for the visited set and queue
'''
from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visit_land = set()
        islands = 0

        def bfs(r,c):
            queue = deque()
            visit_land.add((r,c))
            queue.append((r,c))

            while queue:
                row, col = queue.popleft()
                directions = [(0,1),(-1,0),(1,0),(0,-1)]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and
                        c in range(COLS) and
                        grid[r][c] == "1" and
                        (r,c) not in visit_land):
                        queue.append((r,c))
                        visit_land.add((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit_land:
                    bfs(r, c)
                    islands += 1

        return islands

if __name__ == "__main__":
    s = Solution()
    grid_test1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    grid_test2 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    print(f"expected=1, actual={s.numIslands(grid_test1)}")
    print(f"expected=1, actual={s.numIslands(grid_test2)}")
