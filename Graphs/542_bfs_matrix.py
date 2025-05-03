from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        new_mat = []
        spotted_zeros = deque()

        for row in range(rows):
            new_row = []
            for col in range(cols):

                if mat[row][col] == 0:
                    spotted_zeros.append((row, col))
                    new_row.append(0)
                else:
                    new_row.append(float('inf'))
            new_mat.append(new_row)

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while spotted_zeros:
            r, c = spotted_zeros.popleft()
            for d_row, d_col in directions:
                new_row = r + d_row
                new_col = c + d_col

                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if new_mat[r][c] + 1 < new_mat[new_row][new_col]:
                        new_mat[new_row][new_col] = new_mat[r][c] + 1
                        spotted_zeros.append((new_row, new_col))

        return new_mat

def updateMatrix(mat: List[List[int]]) -> List[List[int]]:

    rows, cols = len(mat), len(mat[0])
    queue = deque()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                queue.append((r, c))
            else:
                mat[r][c] = -1

    while queue:
        cur_row, cur_col = queue.popleft()

        for d_row, d_col in directions:
            new_row, new_col = cur_row + d_row, cur_col + d_col

            if 0 <= new_row < rows and 0 <= new_col < cols and mat[new_row][new_col] == -1:
                mat[new_row][new_col] = mat[cur_row][cur_col] + 1
                queue.append((new_row, new_col))

    return mat



mat = [[0,0,0],
       [0,1,0],
       [1,1,1]]
print(updateMatrix(mat))
a=1