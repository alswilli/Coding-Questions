# 0/1 Knapsack 

''' Top-Down Approach -> Draw recursion tree'''

# Go through each index in the items (vals) array to loop through choices
def helper(vals, ws, remainingWeight, totalItems, currentItem, hashMap):
    # Go until the weight is surpassed or you run out of items
    if currentItem >= totalItems or remainingWeight <= 0:
        return 0
    remainingItems = totalItems - currentItem - 1
    key = (remainingItems, remainingWeight)
    # Check if you have reached point in recursion tree before, and if so return
    if key in hashMap:
        return hashMap[key]
    # If current item will push past weight, then keep the best choices so far
    if remainingWeight < ws[currentItem]:
        hashMap[key] = helper(vals, ws, remainingWeight, totalItems, currentItem+1, hashMap)
    # If the current item fits, then pick the best value from either the best choices so far
    # OR the value of picking the current value and the value after picking it
    else:
        hashMap[key] = max(vals[currentItem] +  helper(vals, ws, remainingWeight-ws[currentItem], totalItems, currentItem+1, hashMap),
                     helper(vals, ws, remainingWeight, totalItems, currentItem+1, hashMap))
    return hashMap[key]

def knapsack1(values, weights, W):
    dp = {}
    maxValue = helper(values, weights, W, len(values), 0, dp)
    return maxValue

''' Bottom Up Approach -> Draw table '''
def knapsack2(values, weights, W):
    dp = [[0 for i in range(W+1)] for j in range(len(values))]
    # print(dp)
    for i in range(len(values)):
        for j in range(1, W+1):
            if i < 1:
                if weights[i] <= j:
                    dp[i][j] = max(dp[i][j], values[i] + dp[i][j - weights[i]])
            else:
                if weights[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], values[i] + dp[i-1][j - weights[i]])
    return dp[len(values)-1][W]




maximum1 = knapsack1([2, 4, 6, 9], [2, 2, 4, 5], 8)
maximum2 = knapsack2([2, 4, 6, 9], [2, 2, 4, 5], 8)
print(maximum1)
print(maximum2)
