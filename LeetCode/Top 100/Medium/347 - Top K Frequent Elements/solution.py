# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         frequency = []
#         output = []
#         hashTable = {}
        
#         for num in nums
#             if not hashTable[num]:
#                 hashTable[num] = 1
#             else:
#                 hashTable[num] += 1
                
# #         for key in hashTable:
# #             heap.heappush(frequency, hashTable[key])
            
# #         for i in range(0, k):
# #             output.append(heap.heappop(frequency))
            
#         output = heap.nlargest(k, )
#         return output
            
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """ 
        count = collections.Counter(nums)   
        return heapq.nlargest(k, count.keys(), key=count.get) 