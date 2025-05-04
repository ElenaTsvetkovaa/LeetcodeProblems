from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        lands = 0
        queue = deque([])

        def bfs():

            DIR = [0, 1, 0, -1, 0]
            while queue:
                row, col = queue.popleft()
                for i in range(4):
                    nr, nc = row + DIR[i], col + DIR[i+1]
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        queue.append((nr, nc))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    grid[row][col] = '0'
                    queue.append((row, col))
                    bfs()
                    lands += 1

        return lands

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","1","0"]
]
print(Solution().numIslands(grid))