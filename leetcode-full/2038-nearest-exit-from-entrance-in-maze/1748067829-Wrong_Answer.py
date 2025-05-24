class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        def bfs(x,y,maz,entrance):
            # print(x,y)
            if (x == 0 or y == 0 or x == len(maz[0])-1 or y == len(maz)-1)and(entrance !=[y,x]) :
                print(x,y)
                return 0
            else:
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                found = []

                for xn,yn in directions:
                    maz[y][x] = "+"
                    xx = x+ xn
                    yy = y+ yn

                    if (xx in range(len(maz[0])) and yy in range(len(maz)) and maz[yy][xx]!="+"):
                        print(xx,yy)
                        tmp = bfs(xx,yy,maz,entrance)
                        if tmp > -1:
                            found.append(tmp)

   
                if len(found)>0:
                    return min(found)+1
                return -1
        to = bfs(entrance[1],entrance[0],maze,entrance)
        
        return to
        


