# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         def wordBreakRecurse(s, wordDict, i):
#             # print(s)
#             while len(s) > 0:
#                 char = s[i]
#                 currWords = []
#                 for word in wordDict:
#                     if char == word[i] and len(word) <= len(s):
#                         currWords.append(word)
#                 # print(currWords)
#                 # break
                
#                 if len(currWords) == 0:
#                     return False

#                 # Now we are working with the current words, so lets run the main algorithm
#                 j = i + 1
#                 isValid = False
#                 for word in currWords:
#                     while j < len(word) and s[j] == word[j]:
#                         j += 1
#                     if j == len(word):
#                         isValid = wordBreakRecurse(s[j:], wordDict, 0)
#                         if isValid == True:
#                             return True
#                     # else:
#                     # Try next word
#                     j = i+1
#                 if isValid is True:
#                     return True
#                 else:
#                     return False
#             return True
        
#         i = 0
#         isValid = False
#         # while len(s) > 0:
#         char = s[i]
#         currWords = []
#         for word in wordDict:
#             if char == word[i] and len(word) <= len(s):
#                 currWords.append(word)
#         # print(currWords)
#         # break

#         if len(currWords) == 0:
#             return False

#         # Now we are working with the current words, so lets run the main algorithm
#         j = i + 1
#         for word in currWords:
#             # print("WROD: " + word + str(j))
#             while j < len(word) and s[j] == word[j]:
#                 # print("lol")
#                 j += 1
#             if j == len(word):
#                 # print("blah")
#                 isValid = wordBreakRecurse(s[j:], wordDict, 0)
#                 # print("here")
#                 if isValid is True:
#                     return True
#             # else:
#                 # Try next word
#             # print("gaga")
#             j = i+1
#         if isValid is True:
#             return True
#         else:
#             return False

# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         # true or false, so dfs backtracing or dynamic programming
#         # dfs(currentString, wordDict)
#         # s length: N, dict length: M
#         # Time O(M^(N/M)) Space(O(1)) ----> quite slow
        
#         # DP approach
#         # breakable[i]: is string[:i] is breakable
#         # if breakable[i], then all breakable[j] (where s[i:j] in wordDict) is also breakable
#         # convert wordDict into set for O(1) lookup
#         # Time: O(N*M) Space(N) where N is len(s) M is len(dict)
        
#         breakable = [None]*(len(s)+1)
#         wordDict = set(wordDict)
        
#         def dp(index):
#             print(index, s[:index])
#             if breakable[index] is not None:
#                 return breakable[index]
#             if s[:index] in wordDict:
#                 breakable[index] = True
#                 return True
#             for word in wordDict:
#                 print(s[index-len(word):])
#                 if s[index-len(word):index] == word:
#                     breakable[index] = dp(index-len(word))
#                     if breakable[index]:
#                         return True

#             return False
        
#         return dp(len(s))

class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(n + 1):
            for word in word_dict:
                if s[i - len(word):i] == word and dp[i - len(word)]:
                    dp[i] = 1
                    break
        return dp[n]