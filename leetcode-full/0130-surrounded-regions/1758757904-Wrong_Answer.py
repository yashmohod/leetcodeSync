class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # border = [(0,0),(0,0),(0,len(board[0])),(len(board),0)]
        visited = set()
        def dfs(x,y):
            dir = [(1,0),(-1,0),(0,-1),(0,1)]
            visited.add((x,y))
            # print(board[y][x] == "O",x,y,board[y][x] )
            if board[y][x] == "O":
                board[y][x] = "1"

            for xd,yd in dir:
                xx = x+xd
                yy = y+yd
                if xx in range(len(board[0])) and yy in range(len(board)) and board[y][x] == "O" and (xx,yy) not in visited:
                    dfs(xx,yy)



        for i in range(len(board)):
            # print(0,i,len(board[0])-1,i)
            dfs(0,i)
            dfs(len(board[0])-1,i)
        for i in range(1,len(board[0])-1):
            # print(0,i,len(board[0])-1,i)
            dfs(i,0)
            dfs(i,len(board)-1)
        
        # for i in board:
        #     print(i)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]== "O":
                    board[i][j]= "X"
                if board[i][j]== "1":
                    board[i][j]="O"


