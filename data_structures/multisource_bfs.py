from typing import List
from collections import deque

class multisource_bfs:
    def solve(self, grid: List[List[str]]) -> None:
        rows = len(grid)
        columns = len(grid[0])
        queue = deque()

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 'D':
                    queue.append((row, column))
                    grid[row][column] = '0'

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # print("queue", queue)
        while queue:
            row , column = queue.popleft()

            for dr, dc in directions:
                nr = row + dr
                nc = column + dc
                if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == ' ':
                    grid[nr][nc] = str(int(grid[row][column]) +  1)
                    queue.append((nr, nc))

        # print(grid)


if __name__ == "__main__":
    grid = [
        ['X', ' ', ' ', 'D', ' ', ' ', 'X', ' ', 'X'],  # 0
        ['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X'], # 1
        [' ', ' ', ' ', 'D', 'X', 'X', ' ', 'X', ' '], # 2
        [' ', ' ', ' ', 'D', ' ', 'X', ' ', ' ', ' '], # 3
        [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X'], # 4
        [' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X', 'X'] # 5
    ]
    bfs = multisource_bfs()
    locations = [ [2, 2], [4, 0], [0, 4], [2, 6] ]
    bfs.solve(grid)

    for r in range(len(grid)):
        print(grid[r])

    for r, c in locations:
        # print(r, c)
        print(grid[r][c])