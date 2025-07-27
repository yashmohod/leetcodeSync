class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        

        fast = slow = slow2 = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        while True:
            if slow == slow2:
                return slow
            slow = nums[slow]
            slow2 = nums[slow2]

        # return slow 
