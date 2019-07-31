class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dubs = {}
        for num in nums:
            if num not in dubs:
                dubs[num] = num
            else:
                del dubs[num]
        
        print(dubs)
        for key in dubs:
            return dubs[key]
                