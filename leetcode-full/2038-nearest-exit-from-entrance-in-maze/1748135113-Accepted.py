class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        been = set()
        q = deque([(entrance[1],entrance[0],0)])
        been.add((entrance[1],entrance[0]))
        ends = []

        while q:
            cur = q.popleft()
            x,y,steps = cur
            maze[y][x] = "+"

            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            for xn,yn in directions:
                xx = xn +x
                yy = yn +y
                
                if (xx in range(len(maze[0])) and 
                    yy in range(len(maze)) and
                    maze[yy][xx] != "+" and
                    (xx,yy) not in been
                    ):
                    if xx == 0 or yy == 0 or xx == len(maze[0])-1 or yy == len(maze)-1:
                        # ends.append(steps+1)
                        # print(xx,yy,steps+1,"found")
                        return steps+1
                        # been.add((xx,yy))
                    else:
                        print(xx,yy)
                        q.append((xx,yy,steps+1))
                        been.add((xx,yy))

        return -1   
        # print(ends)
        # if len(ends) ==0 :
        #     return -1
        # else:
        #     return min(ends)

        


