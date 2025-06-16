class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        while "" in s:
            s.remove("")
        print(s)
        return len(s[-1])

