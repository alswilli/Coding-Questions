class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hTable = {}
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in hTable:
                return [i, hTable[complement]]
            else:
                hTable[nums[i]] = i
                