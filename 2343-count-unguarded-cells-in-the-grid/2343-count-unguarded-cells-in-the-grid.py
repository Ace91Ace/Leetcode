class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        grid = [[0] * n for _ in range(m)]

        for r,c in guards :
            grid[r][c] = 1
        
        for r,c in walls:
            grid[r][c] = 2
        

        def fill(r,c):
            x = r + 1
            y = c + 1

            while x < m:
                if grid[x][c] in [1,2]:
                    break
                grid[x][c] = 3
                x += 1
            x = r - 1
            while x >= 0:
                if grid[x][c] in [1,2]:
                    break
                grid[x][c] = 3
                x -= 1

            while y < n:
                if grid[r][y] in [1,2]:
                    break
                grid[r][y] = 3
                y += 1
            y = c - 1
            while y >= 0:
                if grid[r][y] in [1,2]:
                    break
                grid[r][y] = 3
                y -= 1
        
        for r,c in guards :
            fill(r,c)
        print(grid)
        return sum(cell == 0 for row in grid for cell in row)
