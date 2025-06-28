class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        too = len(nums)-k
        if too <1:
            too = len(nums)

        for i in range(0,too):
            for j in range(1,k+1):
                print(i,j)
                if nums[i+j] == nums[i]:
                    return True
        return False
