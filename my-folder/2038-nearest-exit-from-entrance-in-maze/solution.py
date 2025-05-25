class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        been = set()
        q = deque([(entrance[1],entrance[0],0)])
        been.add((entrance[1],entrance[0]))
        ends = []
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        maze[entrance[0]][entrance[1]] = '+'
        while q:
            cur = q.popleft()
            x,y,steps = cur
            for xn,yn in directions:
                xx = xn +x
                yy = yn +y
                
                if (xx in range(len(maze[0])) and 
                    yy in range(len(maze)) and
                    maze[yy][xx] != "+" and
                    (xx,yy) not in been
                    ):
                    if xx == 0 or yy == 0 or xx == len(maze[0])-1 or yy == len(maze)-1:
                        return steps+1
                    else:
                        q.append((xx,yy,steps+1))
                        been.add((xx,yy))
                        maze[yy][xx] = "+"

        return -1   


        


