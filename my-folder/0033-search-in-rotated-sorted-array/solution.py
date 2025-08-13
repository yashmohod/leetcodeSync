class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bs(ll,rr):
            
            while ll<=rr:
                mm = (ll+rr)//2
                print(ll,mm,rr)
                print(nums[mm] == target)
                if nums[mm] == target:
                    return mm
                elif nums[mm] < target:
                    return bs(mm+1,rr)
                elif nums[mm] > target:
                    return bs(ll,mm-1)
            
            return -1


        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1 


        l,r =0,len(nums)-1
        if nums[l]<nums[r]:
            return bs(l,r)
        else:
            
            while nums[r]>nums[r-1]:
                r-=1
            
            if nums[l] <= target:
                return bs(l,r-1)
            else:
                return bs(r,len(nums)-1)




