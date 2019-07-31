class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        bestSoFar = 0
        currBest = 0
        head = 0
        tail = 0
        negBest = -float('inf')
        # Positive Case
        while tail < len(nums):
            if currBest + nums[tail] > 0:
                currBest += nums[tail]
                tail += 1
            else:
                if currBest + nums[tail] > negBest:
                    negBest = currBest + nums[tail]
                tail += 1
                head = tail
                currBest = 0
                
            if currBest > bestSoFar:
                bestSoFar = currBest
                
        # Check Negative Case
        if bestSoFar == 0 and negBest != -float('inf'):
            return negBest
        
        return bestSoFar