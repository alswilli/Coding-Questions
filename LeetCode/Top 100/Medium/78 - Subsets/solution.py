class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:   
        def recurse(currSeq, index, out):
            if index > len(nums):
                return out
            for i in range(index, len(nums)):
                seq = currSeq + [nums[i]]
                out.append(seq)
                out = recurse(seq, i+1, out)
            return out
        output = []
        output.append([])
        for i in range(0, len(nums)):
            seq = [nums[i]]
            output.append(seq)
            output = recurse(seq, i+1, output)
        return output
        
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         ans=[]
#         def dfs(arr,ind):
#             if ind>=len(nums):
#                 ans.append(arr)
#                 print(ans)
#                 return
#             dfs(arr,ind+1)
#             dfs(arr+[nums[ind]],ind+1)
#         dfs([],0)
#         return ans 