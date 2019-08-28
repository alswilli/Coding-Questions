class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < len(nums):
            # count = 1
            if nums[i] == 0:
                # Another loop to find the num to swap with
                j = i+1
                while j < len(nums) and nums[j] == 0:
                    # count += 1
                    j += 1
                # Swap
                if j < len(nums) and nums[j] != 0:    
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
            # print(nums)
            i += 1