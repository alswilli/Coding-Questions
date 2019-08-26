# class MinStack:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#         self.norm = []

#     def push(self, x: int) -> None:
#         self.norm.append(str(x))
#         print("NORM: " + str(self.norm))
#         heapq.heappush(self.stack, x)

#     def pop(self) -> None:
#         print(self.norm)
#         curr = self.norm.copy()
#         # self.norm = self.norm[:len(self.norm)-1]
#         self.norm.clear()
#         for num in curr[:len(curr) - 1]:
#             self.norm.append(str(num))
#         self.stack = self.norm
#         self.stack.sort()
#         print(self.norm)
#         print(self.stack)
#         print()

#     def top(self) -> int:
#         return int(self.norm[-1])

#     def getMin(self) -> int:
#         return self.stack[0]

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._min_stack = []
        

    def push(self, x: int) -> None:
        if not self._min_stack or x <= self._min_stack[-1]:
            self._min_stack.append(x)
        self._stack.append(x)
        

    def pop(self) -> None:
        if not self._stack:
            raise ValueError("Poping an empty stack")
        if self._stack[-1] == self._min_stack[-1]:
            self._min_stack.pop()
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()