class Solution:
    def canJump(self, nums: List[int]) -> bool:

        cur = 0 

        while cur <= len(nums):
            if cur >= len(nums)-1:
                return True
            else:
                if nums[cur] == 0:
                    return False
            
            toadd =0 
            maxx = float('-inf')
            print("***********")
            print(cur)
            for i in range(nums[cur]+1):
                print("check: ",i,nums[cur+i])
                if cur+i > len(nums):
                    return True
                else:
                    if nums[cur+i] > maxx:
                        toadd = i+1
                        maxx = nums[cur+i]
            print("to add:",toadd)
            cur += toadd
        

