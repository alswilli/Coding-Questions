# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         left = 0
#         right = len(prices)-1
#         lowest = float('inf')
#         highest = -1
        
#         while left < right:
#             if prices[left] < lowest:
#                 lowest = prices[left]
#             if prices[right] > highest:
#                 highest = prices[right]
#             left += 1
#             right -= 1
#         if left == right:
#             if prices[left] < lowest:
#                 lowest = prices[left]
#             if prices[right] > highest:
#                 highest = prices[right]
        
#         if (lowest == float('inf') and highest == -1) or lowest >= highest:
#             return 0
#         return highest - lowest

class Solution:
    def maxProfit(self, prices):
        minprice = float('inf')
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice
        return maxprofit