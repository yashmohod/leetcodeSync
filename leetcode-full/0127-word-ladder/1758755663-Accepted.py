class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        pat ={}

        for word in wordList:
            for i in range(len(word)):
                cpat = word[:i]+"*"+word[i+1:]
                # print(cpat)
                if cpat in pat:
                    pat[cpat].append(word)
                else:
                    pat[cpat]=[word]
        
        q = deque()
        q.append(beginWord)
        visited = set()
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    cpat = word[:i]+"*"+word[i+1:]
                    if cpat in pat:
                        for next in pat[cpat]:
                            if next not in visited:
                                visited.add(next)
                                q.append(next)
            res +=1
        return 0
        
