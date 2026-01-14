class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(y, x, i):
            if i == len(word):
                return True
            if y < 0 or y >= m or x < 0 or x >= n or board[y][x] != word[i]:
                return False

            tmp = board[y][x]
            board[y][x] = "#"  # mark visited

            found = (
                dfs(y+1, x, i+1) or
                dfs(y-1, x, i+1) or
                dfs(y, x+1, i+1) or
                dfs(y, x-1, i+1)
            )

            board[y][x] = tmp  # unmark
            return found

        for y in range(m):
            for x in range(n):
                if dfs(y, x, 0):
                    return True
        return False

