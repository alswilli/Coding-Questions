class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        large = []
        for num in nums:
            if len(large) < k:
                heapq.heappush(large, num)
            else:
                for i in range(0, len(large)):
                    if large[i] < num:
                        heapq.heappushpop(large, num)
                        break
            # print(large)
        return large[0]