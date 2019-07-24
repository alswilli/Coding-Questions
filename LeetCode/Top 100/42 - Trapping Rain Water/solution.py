class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        total = 0
        leftMax = 0
        rightMax = 0
        
        while left < right:
            print(height[left])
            print(height[right])
            if height[left] < height[right]:
                print('left')
                if height[left] < leftMax:
                    total += leftMax - height[left]
                elif height[left] >= leftMax:
                    leftMax = height[left]  
                left += 1
            elif height[right] <= height[left]:
                print('right')
                if height[right] < rightMax:
                    total += rightMax - height[right]
                elif height[right] >= rightMax:
                    rightMax = height[right]
                right -= 1
            print()
                
        return total