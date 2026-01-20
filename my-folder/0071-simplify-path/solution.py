class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path = path.split("/")
        while "" in path or " " in path:
            if "" in path : 
                path.remove("")
            if " " in path : 
                path.remove(" ") 

        s = []

        for i in path:
            if i =="..":
                if len(s)>0:
                    s.pop()
            elif i == ".":
                continue
            else:
                s.append(i)

        return "/"+"/".join(s)  
