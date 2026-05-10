class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        q = deque([])
        for y in range(len(board)):
            for x in range(len(board[0])):
                if (y in [0,len(board)-1] or x in [0,len(board[0])-1]) and board[y][x] =="O":
                    board[y][x] ="-1"
                    q.append((x,y))
        dirs=[[0,-1],[0,1],[-1,0],[1,0]]
        
        while q:
            x,y = q.popleft()
            for dx,dy in dirs:
                if 0<=dx+x< len(board[0]) and 0<=dy+y< len(board) and board[dy+y][dx+x] =="O":
                    board[dy+y][dx+x] ="-1"
                    q.append((dx+x, dy+y))
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] != "-1":
                    board[y][x] = "X"
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == "-1":
                    board[y][x] = "O"
                    


        
