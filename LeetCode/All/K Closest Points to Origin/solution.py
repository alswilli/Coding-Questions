import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def modifyDistance(x, y):
            print(pow(x, 2) + pow(y, 2))
            print(x**2 + y**2)
            return pow(x, 2) + pow(y, 2)
        
        heap = []
        for p in points:
            heapq.heappush(heap, (modifyDistance(p[0], p[1]), p))
            
        ans = []
        for _ in range(K):
            ans.append(heapq.heappop(heap)[1])
            
        return ans