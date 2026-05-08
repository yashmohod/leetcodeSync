class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        count = 0

        coins.sort(reverse=True)

        for coin in coins:
            print(count,amount,coin)
            if amount < coin:
                continue
            count += amount // coin
            amount = amount % coin
        return count if amount ==0 else -1
