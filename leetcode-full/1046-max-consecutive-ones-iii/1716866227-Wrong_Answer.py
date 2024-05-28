class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start=0
        end = 0
        la =0

        while end<len(nums):
            if k == 0:
                while nums[start] !=0:
                    start+=1
                    la-=1
                start+=1
                la-=1
                k+=1

            if nums[end] == 0:
                k-=1
            la+=1
            end+=1
        return la

