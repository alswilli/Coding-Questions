class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0] * len(T)
        stack = []
        
        for i in range(0, len(T)):
            while (len(stack) > 0 and T[i] > T[stack[len(stack)-1]]):
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
        
        return result