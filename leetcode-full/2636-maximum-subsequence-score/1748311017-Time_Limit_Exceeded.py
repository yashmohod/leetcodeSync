class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        subz=[]
        def comb(cd,ad,used,fromto,subs):
            if cd < ad:
                for i in fromto:
                    if fromto.index(i) not in used:
                        tmp = used.copy()
                        tmp.append(fromto.index(i))
                        comb(cd+1,ad,tmp,fromto,subs)
            else:
                subs.append(used)
        comb(0,k,[],range(len(nums1)),subz)

        # print(subz)

        maxN = -float('inf')
        for sub in subz:
            sum = 0

            for i in sub:
                sum += nums1[i]

            minN = float('inf')
            for i in sub:
                if nums2[i] < minN:
                    minN = nums2[i]
            
            if maxN < minN * sum:
                maxN = minN * sum

        return maxN
