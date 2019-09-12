# class Solution:
#     def climbStairs(self, n: int) -> int:
#         def recurse(n, currTotal=0):
#             if currTotal > n:
#                 return
#             elif currTotal == n:
#                 self.ans += 1
#             else:
#                 # retVal = True
#                 for i in range(0, len(options)):
#                     recurse(n, currTotal+options[i])
        
#         options = [1, 2]
#         self.ans = 0
#         recurse(n)
#         # count = recurse(n, count)
#         return self.ans

class Solution:
    def climbStairs(self, n: int) -> int:
        def recurse(n, currTotal=0):
            if currTotal > n:
                return 0
            elif currTotal == n:
                # self.ans += 1
                return 1
            elif memo[currTotal] > 0:
                return memo[currTotal]
                # retVal = True
            for i in range(0, len(options)):
                memo[currTotal] += recurse(n, currTotal+options[i])
            return memo[currTotal]
        
        options = [1, 2]
        # self.ans = 0
        # memo = [[]]
        # memo = [[0 for x in range(5)] for y in range(4)]
        memo = [0 for x in range(n+1)]
        # count = recurse(n, count)
        return recurse(n)