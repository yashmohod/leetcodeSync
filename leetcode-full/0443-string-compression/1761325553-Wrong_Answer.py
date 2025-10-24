class Solution:
    def compress(self, chars: List[str]) -> int:
        
        st = {}

        for i in chars:
            st[i] = st.get(i,0)+1
        res = ""
        c=0
        for x,y in st.items():
            if y == 1:
                res+=x
            else:
                res+=x+str(y)

        for i,j in enumerate(res):
            chars[i]=j

        return len(res)
