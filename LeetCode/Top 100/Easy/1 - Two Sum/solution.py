class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hTable = {}
        # for i in range(0, len(nums)):
        #     complement = target - nums[i]
        #     if complement in hTable:
        #         return [i, hTable[complement]]
        #     else:
        #         hTable[nums[i]] = i
        
        
        
        
        
        dict = {}
        output = None
        for i, val in enumerate(nums):
            dict[target - val] = i
            
        for j, val in enumerate(nums):
            if val in dict and j != dict[val]:
                output = [j, dict[val]]
                
#         dict = {}
#         output = None
#         for i, val in enumerate(nums):
#             dict[target - val] = i
            
#         for j, val in enumerate(nums):
#             if val in dict and j != dict[val]:
#                 output = [j, dict[val]]
        
        return output