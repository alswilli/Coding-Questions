class Solution:
#     def reverse(self, s):
#         sPrime = ""
#         i = len(s) - 1
#         while i >= 0:
#             sPrime = sPrime + s[i]
#             i -= 1
#         return sPrime
    
#     def longestPalindrome(self, s: str) -> str:
#         sPrime = self.reverse(s)
#         # print(sPrime)
#         i = 0
#         # j = 0
#         longest = ""
        
#         # while i < len(s):
#         #     if s[i] == sPrime[i]:
#         #         curr = ""
#         #         start = i
#         #         while i < len(s) and s[i] == sPrime[i]:
#         #             curr = curr + s[i]
#         #             i += 1
#         #         check = (len(s) - 1) - (i - 1)
#         #         if len(curr) > len(longest) and check == start:
#         #             longest = curr
#         #     i += 1
        
#         while i < len(s):
#             if s[i] == sPrime[i]:
#                 curr = ""
#                 start = i
#                 while i < len(s) and s[i] == sPrime[i]:
#                     curr = curr + s[i]
#                     i += 1
#                 check = (len(s) - 1) - (i - 1)
#                 if len(curr) > len(longest) and check == start:
#                     longest = curr
#             elif i+1 < len(s) and s[i+1] == sPrime[i]:
#                 curr = ""
#                 start = i
#                 while i+1 < len(s) and s[i+1] == sPrime[i]:
#                     curr = curr + s[i+1]
#                     i += 1
#                 check = (len(s) - 1) - ((i+1) - 1)
#                 if len(curr) > len(longest) and check == start:
#                     longest = curr
#             elif i+1 < len(s) and s[i] == sPrime[i+1]:
#                 curr = ""
#                 start = i+1
#                 while i+1 < len(s) and s[i] == sPrime[i+1]:
#                     curr = curr + s[i]
#                     i += 1
#                 check = (len(s) - 1) - (i - 1)
#                 if len(curr) > len(longest) and check == start:
#                     longest = curr
#             i += 1
        
#         if longest == "" and len(s) > 0:
#             longest = s[0]
#         return longest

    def longestPalindrome(self, s: str) -> str:
        dp = collections.defaultdict(lambda : collections.defaultdict(lambda : 0))
        maxPalindrome = 0
        ans = ""
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if(j-i == j):
                    dp[j-i][j] = 1
                elif(not dp[j-i+1][j-1] == -1 and s[j-i] == s[j] ):
                    dp[j-i][j] = 2 + dp[j-i+1][j-1]
                else:
                    dp[j-i][j] = -1
                if(dp[j-i][j] > maxPalindrome):
                    maxPalindrome = dp[j-i][j]
                    ans = s[j-i:j+1]
        return ans 
    
    # or use this https://www.cs.usfca.edu/~galles/visualization/DPLCS.html

#     def longestPalindrome(self, s): 
#         n = len(s)
#         if n == 0 or n == 1: 
#             return s
#         start = -1
#         end = -1
#         P = [[False for i in range(n)] for j in range(n)]
#         # print(P)
        
#         for i in range(0, n):
#             P[i][i] = True
#             start = i
#             end = i
            
#         for i in range(0, n-1):
#             if s[i] == s[i+1]:
#                 P[i][i+1] = True
#                 start = i
#                 end = i

#         for j in range(2, n):
#             i = 0;
#             k = j;
#             while k < n:
#                 P[i][k] = P[i+1][k-1] and (s[i] == s[k])
#                 if P[i][k] and (k-i) > (end-start): 
#                     start = i
#                     end = k
#                 k += 1
#                 i += 1

#         print(start)
#         print(end)
#         return s[start:end-start+1]
    
    
    