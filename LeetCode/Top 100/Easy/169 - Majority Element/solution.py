class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashTable = {}
        maj = int(len(nums) / 2)
        
        for num in nums:
            if num in hashTable:
                hashTable[num] += 1
                if hashTable[num] > maj:
                    return num
            else:
                hashTable[num] = 1
                
        return nums[0]