class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums.reverse()
        cur = 0 

        while cur <= len(nums):
            if cur >= len(nums)-1:
                return True
            else:
                if nums[cur] == 0:
                    return False
            
            toadd =0 
            maxx = float('-inf')
            for i in range(1,nums[cur]+1):

                if cur+i >= len(nums)-1 or nums[cur+i] >= len(nums)-1:
                    return True
                else:
                    if nums[cur+i] >= maxx or i > toadd:
                        toadd = i
                        maxx = nums[cur+i]

            cur += toadd
        

