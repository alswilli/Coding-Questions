class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        foundNums = {}
        output = []
        for i in range(1, len(nums) + 1):
            output.append(i)
        print(output)
        for num in nums:
            foundNums[num] = "found"
        print(foundNums)
        i = 0
        while i < len(output):
            if output[i] in foundNums:
                del output[i]
            else:
                i += 1
                
                
        return output
    
# class Solution(object):
#     def findDisappearedNumbers(self, a):
#         for i in range(len(a)):
#             j = a[i]
#             while j != a[j-1]:
#                 a[j-1], j = j, a[j-1]
#         return [i+1 for i in range(len(a)) if a[i] != i+1]