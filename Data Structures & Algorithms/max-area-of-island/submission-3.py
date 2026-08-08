class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        maxAmount = 0

        def bfs(r,c):
            nonlocal maxAmount
            queue = deque([(r,c)])
            grid[r][c] = 0
            counter = 1
            while queue:
                (r,c) = queue.popleft()
                for dr, dc in directions:
                    nr,nc = dr + r, dc + c
                    if nr<0 or rows<=nr or nc<0 or cols<= nc or grid[nr][nc] == 0:
                        continue
                    queue.append((nr,nc))
                    grid[nr][nc] = 0
                    counter +=1
            return counter

                    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxAmount = max(maxAmount,bfs(r,c)) 
        return maxAmount
        