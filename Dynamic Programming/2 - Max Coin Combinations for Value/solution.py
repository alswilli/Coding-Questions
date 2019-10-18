# Coin Change 2 - https://leetcode.com/problems/coin-change-2/

''' Top-Down Approach -> Draw recursion tree'''
    if not array and target == 0:
        return 1
    
    if not array and target > 0:
        return 0
    
    row = len(array)

    column = target

    matrix = [[0 for i in range(column+1)] for j in range(row)]

    for row in matrix:
        row[0] = 1

    first = array[0]

    for j in range(1, target+1):
        if j % first == 0:
            matrix[0][j] = 1

    for item in range(1, target+1):
        for index in range(1, len(array)):
            if item >= array[index]:
                matrix[index][item] = matrix[index-1][item] + matrix[index][item-array[index]]
            else:
                matrix[index][item] = matrix[index-1][item]

    return matrix[-1][-1]
# def helper(a, c, dp):
#     if a < 0 or len(coins) == 0:
#         return 0
    
#     if a == 0:
#         return 1
    
#     key = (a, c)
#     if key in dp:
#         return dp[key]

#     if c[-1] > a:
#         dp[key] = helper(amount, c[:-1], dp)
#     else:
#         dp[key] = helper(amount-c[-1], c, dp) + helper(amount, c[:-1], dp)
#     return dp[key]

# def solution1(amount, coins):
#     hashTable = {}
#     maxWays = helper(amount, coins, hashTable)
#     return maxWays

''' Bottom Up Approach -> Draw table '''
def solution2(amount, coins):
    dp = [[0 for i in range(amount+1)] for j in range(len(coins))]

    if len(coins) == 0:
        if amount == 0:
            return 1
        return 0

    for i in range(len(coins)):
        dp[i][0] = 1 # can always make 0

    for i in range(len(coins)):
        for j in range(1, amount+1):
            if i < 1:
                if coins[i] <= j:
                #     dp[i][j] = max(1, 1 + dp[i][j - coins[i]])
                    dp[i][j] = dp[i][j - coins[i]]
            else:
                if coins[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    # Take coin, stay in row. Don't take, drop to lower row
                    # Essentially, you have two recursive splits (try using coin again or go to other coins) so need to sum them
                    dp[i][j] = dp[i][j-coins[i]] + dp[i-1][j]
    return dp[len(coins)-1][amount]




# num1 = solution1(5, [1,2,5])
num2 = solution2(5, [1,2,5])
# print(maximum1)
print(num2)