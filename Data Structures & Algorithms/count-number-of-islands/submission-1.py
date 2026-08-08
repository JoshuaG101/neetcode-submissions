class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(r,c):
            queue = deque([(r,c)])
            grid[r][c] = "0"
            while queue:
                r,c = queue.popleft()
                for dr, dc in directions:
                    nr,nc = dr + r, dc +c
                    if 0>nr or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == "0":
                        continue
                    queue.append((nr,nc))
                    grid[nr][nc] = "0"
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands +=1
        return islands