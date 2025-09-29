class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        count = 0
        coins.sort(reverse=True)
        c=0

        while c < len(coins):
            if amount < coins[c]:
                c+=1
            else:
                amount -=coins[c]
                count+=1

        if amount ==0:
            return count
        else:
            return -1
