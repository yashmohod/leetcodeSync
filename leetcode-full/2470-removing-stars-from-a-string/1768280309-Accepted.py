class Solution:
    def removeStars(self, s: str) -> str:
        st = deque([])

        for i in s :
            if i == "*":
                st.pop()
            else:
                st.append(i)
        return "".join(st)
