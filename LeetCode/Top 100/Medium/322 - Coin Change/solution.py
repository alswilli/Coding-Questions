### OLD SOLUTION
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         n = len(coins)
#         if n == 0:
#             return 0

#         coins.sort()
#         dp = [-1 for _ in range(amount + 1)]
#         dp[0] = 0

#         for coin in coins:
#             for j in range(0, amount + 1):
#                 if j >= coin and dp[j-coin] != -1:
#                     dp[j] = (1 + dp[j-coin]) if (dp[j] == -1) else min(dp[j], 1 + dp[j-coin])
#         return  dp[-1]

# ### SOLUTION WITHOUT DP -> BACKTRACKING
# class Solution:
#     def recurse(self, coins, amount, val = 0, count = 0, minCount = float('inf'), combo = []):
#         # print("Min = " + str(minCount))
#         # print("Level = " + str(count))
#         # print("Current val = " + str(val))
#         for coin in coins:
#             # print("Min = " + str(minCount))
#             # print("Level = " + str(count))
#             # print("Current val = " + str(val))
#             # print(combo+[coin])
#             # print()
#             if val + coin > amount:
#                 # print("GREATER")
#                 # print(" ")
#                 # return minCount
#                 break
#             elif val + coin == amount:
#                 count += 1
#                 # print("EQUAL")
#                 # print(" ")
#                 # break
#                 return count
#             elif val + coin < amount:
#                 # print("LESS")
#                 # print(" ")
#                 # combo.append(coin)
#                 minCount = min(minCount, self.recurse(coins, amount, val + coin, count + 1, minCount, combo+[coin]))
#         # print("here")
#         return minCount
    
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         memo = [[0 for _ in range(0, amount+1)] for _ in range(0, len(coins))]
#         # print(dp)
#         num = self.recurse(coins, amount)
#         if amount == 0:
#             return 0
#         elif num == float('inf'):
#             return -1
#         return num

# # coins = [1, 2, 5]
# # amount = 11
# # sol = Solution()
# # ret = sol.coinChange(coins, amount)
# # print(ret)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = [0 in range(amount+1)]
        # print(ans)
        
        for currAmount in range(1, len(ans)):
            for coinAmount in coins:
                if coinAmount <= currAmount:
                    print (coinAmount)
                    ans[currAmount] = min(1 + ans[currAmount - coinAmount], ans[currAmount])
        
        print(ans)
        return ans[-1]


# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if amount == 0:
#             return 0
#         if (not coins) or (min(coins) > amount) or (len(coins)==1 and amount%coins[0]!=0):
#             return -1
        
#         res = self.helper(coins, amount, {})
#         if res > amount:
#             return -1
#         else:
#             return res
        
#     def helper(self, coins, n, cache):
#         if n == 0:
#             return 0
#         elif n in cache:
#             return cache[n]
        
#         cache[n] = float('inf')
#         for coin in coins:
#             if coin <= n:
#                 cache[n] = min(cache[n], 1 + self.helper(coins, n-coin, cache))
#         return cache[n]
    
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if amount == 0:
#             return 0
#         if (not coins) or (min(coins) > amount) or (len(coins)==1 and amount%coins[0]!=0):
#             return -1
        
#         dp = [amount+1]*(amount+1)
#         dp[0] = 0
        
#         for i in range(1, amount+1):
#             for coin in coins:
#                 if coin <= i:
#                     dp[i] = min(dp[i], 1 + dp[i-coin])

#         if dp[amount] > amount:
#             return -1
#         else:
#             return dp[amount]