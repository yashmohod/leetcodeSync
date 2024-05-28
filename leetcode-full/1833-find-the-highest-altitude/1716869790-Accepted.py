class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sum = 0
        la =0
        for i in gain:
            sum += i
            la = max(la,sum)
        return la
