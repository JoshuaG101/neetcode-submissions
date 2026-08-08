from collections import deque
from typing import List


class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        max_amount = 0

        def bfs(r, c) -> int:
            queue = deque([(r, c)])
            grid[r][c] = 0  # Mark as visited
            area = 1  # Start at 1 for the starting cell

            while queue:
                curr_r, curr_c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = curr_r + dr, curr_c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == 1
                    ):
                        queue.append((nr, nc))
                        grid[nr][nc] = 0  # Mark visited upon enqueueing
                        area += 1

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_amount = max(max_amount, bfs(r, c))

        return max_amount