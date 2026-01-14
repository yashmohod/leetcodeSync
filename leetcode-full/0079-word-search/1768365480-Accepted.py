class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(idx, x, y, seen):
            if idx == len(word) - 1:
                return True

            for dx, dy in dirs:
                xx, yy = x + dx, y + dy

                if (
                    0 <= xx < n and 0 <= yy < m and
                    (yy, xx) not in seen and
                    board[yy][xx] == word[idx + 1]
                ):
                    seen.add((yy, xx))
                    if dfs(idx + 1, xx, yy, seen):
                        return True
                    seen.remove((yy, xx))

            return False

        for y in range(m):
            for x in range(n):
                if board[y][x] == word[0]:
                    seen = {(y, x)}
                    if dfs(0, x, y, seen):
                        return True

        return False

