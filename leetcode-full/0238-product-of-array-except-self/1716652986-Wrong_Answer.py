class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = 1
        for i in nums:
            if i !=0:
                product = i*product
        ans=[]
        for i in nums:
            if i ==0:
                ans.append(product) 
            else:  
                if 0 in nums:
                    ans.append(0)
                else: 
                    ans.append(product/i)
        return ans

        
        
