# class Solution:
#     def backtrack(self, edit, nums, answer):
#         if len(edit) == len(nums):
#             answer.append(edit)
#             return answer
#         answer = backtrack(edit, nums, answer)
        
    
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         answer = []
#         answer = backtrack(edit, nums, answer)
#         return answer

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0):
            # if all integers are used up
            if first == n:  
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first 
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        output = []
        backtrack()
        return output