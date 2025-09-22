class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        tobe = image[sr][sc]

        q = deque()
        q.append((sr,sc))
        seen = set()
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            r,c = q.popleft()
            seen.add((r,c))
            if image[r][c] == tobe:
                image[r][c] = color
                for rd,cd in dirs:
                    if r+rd in range(len(image)) and c+cd in range(len(image[0])) and (r+rd,c+cd) not in seen:
                        q.append((r+rd,c+cd))
        
        return image
