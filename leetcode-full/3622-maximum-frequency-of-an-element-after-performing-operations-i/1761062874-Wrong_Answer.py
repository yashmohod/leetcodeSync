class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
    
        nums.sort()
        i = 0
        n = len(nums)
        maxFreq =0
        while i < n:
            target = nums[i]
            j=i
            ic=0
            while j < n :
                if nums[j]-target <k:
                   ic +=1
                j+=1

            lb = target - k 
            rb = target + k
            sidx = bisect_left(nums,lb)
            eidx = bisect_right(nums,rb)

            potentialS = eidx - sidx
            convertible = potentialS - ic
            ops = min(convertible, numOperations)
            curF = ops+ic
            maxFreq = max(curF,maxFreq)
            i+=1
        return maxFreq




