class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]*len(nums)
        answer[0] = 1
        for i in range(1, len(nums)):
            answer[i] = answer[i-1] * nums[i-1]
        rightProduct = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] = answer[i] * rightProduct
            rightProduct *= nums[i]
        return answer

# or instead of division use logs

# We can utilize properties of log, if input array is [a, b, c, d] then
# precalculated_val = log(a* b* c* d) = log(a) + log(b) + log(c) + log(d)
# So for output array it would be { antilog [precalculated_val - log(arr[i])] }