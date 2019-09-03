# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         def recurse(output, currSum, currNums):
#             if currSum == target:
#                 print("EQUAL: " + str(currNums))
#                 # preOutput = output + [currNums]
#                 # if len(set(list(preOutput))) == 1:
#                 #     output.append(list(currNums))
#                 output.append(list(currNums))
#                 return output
#             elif currSum > target:
#                 print("GREATER: " + str(currNums))
#                 return output
#             elif currSum < target:
#                 print("LESS: " + str(currNums))
#                 # print(output)
#                 nextSum = currSum
#                 nextNums = list(currNums)
#                 # output = output
#                 for num in candidates:
#                     nextNums.append(num)
#                     nextSum += num
#                     output = recurse(output, nextSum, nextNums)
#                     nextSum = currSum
#                     del nextNums[-1]
#                 return output
                
#         output = []
#         currSum = 0
#         currNums = []
#         isValid = False
#         savedOutput = []
        
#         for num in candidates:
#             # Look for all the valid combinations where you have to include this number
#             currNums.append(num)
#             currSum += num
#             output = recurse(output, currSum, currNums)
#             currSum = 0
#             currNums.pop()
#             # savedOutput = output
#             # isValid = recurse(output, currSum, currNums)
#             # if isValid is True:
                 
#         return output

# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         def recurse(target, i, currNums, results):
#             for j in range(i, len(candidates)):
#                 candidate = candidates[j]
#                 print("CANDIDATE: " + str(candidate))
#                 print("TARGET: " + str(target))
#                 if candidate > target:
#                     print("GREATER: " + str(currNums))
#                     break
#                 # currNums += [candidate]
#                 currNums.append(candidate)
#                 # print(currNums)
#                 if candidate < target:
#                     print("LESS: " + str(currNums))
#                     print(j)
#                     recurse(target - candidate, j, currNums, results)
#                 else:
#                     print("EQUAL: " + str(currNums))
#                     results.append(list(currNums))
#                 currNums.pop()
#             return
        
#         candidates.sort()
#         output = []
#         # currSum = 0
#         currNums = []
#         recurse(target, 0, currNums, output)
#         return output
        


# class Solution:
#     def combinationSum(self, canidates, target):
#         canidates.sort()
#         results = []
#         self.combinationSumHelper(target, 0, [], results, canidates)
#         return results
    
#     def combinationSumHelper(self, target, i, combo, results, canidates):
#         for j in range(i, len(canidates)):
#             canidate = canidates[j]
#             if canidate > target:
#                 break
#             combo += [canidate]
#             if canidate < target:
#                 self.combinationSumHelper(target - canidate, j, combo, results, canidates)
#             else:
#                 results.append(list(combo))
#             combo.pop()
#         return

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def recurse(sum, currSeq, index, out):
            if index > len(candidates):
                return out
            for i in range(index, len(candidates)):
                num = sum + candidates[i]
                seq = currSeq + [candidates[i]]
                print(seq)
                if num > target:
                    return out
                elif num == target:
                    out.append(seq)
                output = recurse(num, seq, i, out)
                # seq = currSeq + [nums[i]]
                # out.append(seq)
                # out = recurse(seq, i+1, out)
            return out
        output = []
        candidates.sort()
        for i in range(0, len(candidates)):
            num = candidates[i]
            seq = [num]
            if num > target:
                return output
            elif num == target:
                output.append(seq)
            output = recurse(num, seq, i, output)
        return output