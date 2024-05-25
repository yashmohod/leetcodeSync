class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        b=[1]
        cb=1
        a=[1]
        ca=1
        for i in range(len(nums)-1):
            cb*=nums[i]
            b.append(cb)
            ca*=nums[-(i+1)]
            a.append(ca)
        ans=[]
        for i in range(len(b)):
            ans.append(b[i]*a[-(i+1)])
        
        return ans
      
        
