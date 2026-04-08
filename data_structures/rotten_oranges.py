from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        rows = len(grid)
        columns = len(grid[0])

        queue = deque()

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 2:
                    queue.append((row, column, 0))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        time_elapsed = 0
        while queue:
            # print(queue)
            row, column, minutes = queue.popleft()
            time_elapsed = minutes
            for dr, dc in directions:
                nr = row + dr
                nc = column + dc

                if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 1:
                    queue.append((nr, nc, minutes + 1))
                    grid[nr][nc] = 2

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 1:
                    time_elapsed = -1
                    break

        return time_elapsed

