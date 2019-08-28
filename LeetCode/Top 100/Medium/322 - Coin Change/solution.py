class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        if n == 0:
            return 0

        coins.sort()
        dp = [-1 for _ in range(amount + 1)]
        dp[0] = 0

        for coin in coins:
            for j in range(0, amount + 1):
                if j >= coin and dp[j-coin] != -1:
                    dp[j] = (1 + dp[j-coin]) if (dp[j] == -1) else min(dp[j], 1 + dp[j-coin])
        return  dp[-1]