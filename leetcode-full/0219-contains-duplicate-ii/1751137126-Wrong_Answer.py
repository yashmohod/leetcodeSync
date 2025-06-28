class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        for i in range(k,len(nums)):
            for j in range(1,k+1):
                if nums[i-j] == nums[i]:
                    # print(i,j)
                    return True
        return False
