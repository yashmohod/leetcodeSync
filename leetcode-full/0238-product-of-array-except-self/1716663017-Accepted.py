class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        b=[1]
        c=1
        for i in range(len(nums)-1):
            c*=nums[i]
            b.append(c)
        a=[1]
        c=1
        for i in range(len(nums)-1):
            c*=nums[-(i+1)]
            a.append(c)
        ans=[]
        for i in range(len(b)):
            ans.append(b[i]*a[-(i+1)])
        
        return ans
      
        
