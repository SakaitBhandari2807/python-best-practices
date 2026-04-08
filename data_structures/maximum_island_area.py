

def solve(grid):
    visited = set()
    rows = len(grid)
    columns = len(grid[0])

    def dfs(row, column):
        if not (0 <= row < rows and 0 <= column < columns and grid[row][column] == 1 and not (row, column) in visited):
            return 0
        visited.add((row, column))
        return 1 + dfs(row - 1 , column) + dfs(row, column - 1) + dfs(row + 1, column) + dfs(row, column + 1)


    maximum_area = float("-inf")
    for row in range(rows):
        for column in range(columns):
            maximum_area = max(maximum_area, dfs(row, column))

    return maximum_area

def solve_with_grid_change(grid):
    island_id = 2
    rows, columns = len(grid), len(grid[0])
    maximum_area = 0
    def dfs(r, c):

        if r < 0 or r == rows or c < 0 or c == columns or grid[r][c] == 0 or grid[r][c] != 1:
            return 0
        size = 1
        grid[r][c] = island_id
        for dr, dc in [(0,1), (1,0), (0, -1), (-1, 0)]:
            nr = r + dr
            nc = c + dc
            size += dfs(nr, nc)
        return size
    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 1:
                maximum_area = max(maximum_area, dfs(row, column))
                island_id += 1
    return maximum_area

def solve_with_grid_changes_atmost_one_change(grid):
    rows, columns = len(grid), len(grid[0])
    islands = {}
    island_id = 2
    directions = [(0,1), (1,0), (0, -1), (-1, 0)]

    def dfs(r, c):
        if not(0 <= r < rows and 0 <= c < columns and grid[r][c] == 1):
            return 0
        size = 1
        grid[r][c]= island_id

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            size += dfs(nr, nc)
        return size


    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 1:
                islands[island_id] = dfs(row, column)
                island_id += 1

    maximum_area = max(islands.values())

    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == 0:
                neighbours = set()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0<= nr < rows and 0<= nc < columns and grid[nr][nc]>1:
                        neighbours.add(grid[nr][nc])
                maximum_area= max(maximum_area, 1 + sum(islands[i] for i in neighbours))

    return maximum_area



if __name__ == "__main__":
    grid = [[1,0,1,1], [1,0,1,1], [1,0,0,1],[1,0,1,1]]

    print(solve(grid))
    print(solve_with_grid_change(grid))
    grid = [[1,0,1,1], [1,0,1,1], [1,0,0,1],[1,0,1,1]]
    print(solve_with_grid_changes_atmost_one_change(grid))