class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxArea = -1
        
        for h in height:
            area = min(height[i], height[j]) * (j-i)
            if area > maxArea:
                maxArea = area
                
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            
        return maxArea