class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n=len(nums)
        ans=[0]*n

        i,i2=0,0
        j,j2=n-1,n-1

        while i<n:
            if nums[i]<pivot:
                ans[i2]=nums[i]
                i2+=1
            if nums[j]>pivot:
                ans[j2]=nums[j]
                j2-=1
            i+=1
            j-=1

        while i2<= j2:
            ans[i2]=pivot
            i2+=1
        
        return ans


