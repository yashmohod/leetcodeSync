class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) == 0 :
            return -1

        if len(haystack) == 1:
            if haystack[0] == needle:
                return 0
            else:
                return -1

        for i in range(len(haystack)):
            if len(needle) ==1 :
                if needle == haystack[i]:
                    return i
            else:
                if i+len(needle) in range(len(haystack)):
                    print(haystack[i:i+len(needle)])
                    if needle == haystack[i:i+len(needle)]:
                        return i

        return -1

