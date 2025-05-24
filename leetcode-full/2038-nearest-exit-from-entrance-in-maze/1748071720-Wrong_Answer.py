class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = set()
        def bfs(x,y,maz,entrance,visit):
            # print(x,y)
            visit.add((x,y))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            found = []
            tmepp=[]
            for xn,yn in directions:
                
                xx = x+ xn
                yy = y+ yn

                if (xx in range(len(maz[0])) and yy in range(len(maz)) and maz[yy][xx]!="+" and (xx,yy) not in visit):
                    if (xx == 0 or yy == 0 or xx == len(maz[0])-1 or yy == len(maz)-1)and(entrance[0] != yy or entrance[1] != xx ) :
                        print(x,y)
                        return 1
            
                if (xx in range(len(maz[0])) and yy in range(len(maz)) and maz[yy][xx]!="+" and (xx,yy) not in visit):
                    tmp = bfs(xx,yy,maz,entrance,visit)
                    
                    if tmp > 0:
                        found.append(tmp)
                        tmepp.append((xx,yy))

            if len(found)>0:
                # print(tmepp)
                # print("min",min(found)+1)
                return min(found)+1
            return -1        
        print(entrance[1],entrance[0])
        print(len(maze[0])-1,len(maze)-1)
        # for i in maze:
        #     print(i)
        return bfs(entrance[1],entrance[0],maze,entrance,visited)
        


