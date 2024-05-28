class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        start = 0
        end = len(nums)-1
        ls=0
        rs=0
        while start<end:
            if ls == rs:
                ls+= nums[start]
                rs+= nums[end]
                start+=1
                end-=1
            elif ls > rs:
                rs+=nums[end]
                end-=1
            elif ls < rs:
                ls+=nums[start]
                start+=1
        print(start,end,ls,rs)
        if ls == rs:
            return start
        else:
            cur = 0 
            for i in nums[1:]:
                cur+=i
            if cur == 0 :
                return 0 
            
            return -1
