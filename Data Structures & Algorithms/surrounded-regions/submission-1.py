class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])
        safe_cells = set()

        def dfs(r: int, c: int) -> None:
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or board[r][c] != "O"
                or (r, c) in safe_cells
            ):
                return

            safe_cells.add((r, c))

            # Explore all 4 adjacent directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. Run DFS on first and last rows
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)

        # 2. Run DFS on first and last columns
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)

        # 3. Traverse grid: flip 'O' to 'X' if not marked safe
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in safe_cells:
                    board[r][c] = "X"