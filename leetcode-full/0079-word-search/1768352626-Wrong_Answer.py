class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dr = [[1,0],[-1,0],[0,1],[0,-1]] 
        def dfs(idx,x,y,seen):
            if idx == len(word)-1:
                return True
            
            for dx,dy in dr:
                xx = x + dx
                yy = y + dy

                if idx + 1 < len(word) and xx < len(board[0]) and yy < len(board) and (not (xx,yy) in seen) and board[yy][xx] == word[idx+1]:
                    seen.add((xx,yy)) 
                    if dfs(idx+1,xx,yy,seen):
                        return True
                    seen.remove((xx,yy)) 
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(0,j,i,set()):
                        return True
        return False

