class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        finalCount = 0
        count = 0
        i = 0
        while i < len(s):
            dictionary = []
            while i < len(s):
                if s[i] not in dictionary:
                    dictionary.append(s[i])
                    count += 1
                    i += 1
                else:
                    num = dictionary.index(s[i])
                    sub = len(dictionary) - num - 1
                    if finalCount < count:
                        finalCount = count
                    count = 0
                    #edit i
                    i = i - sub
                    break
        if finalCount < count:
            finalCount = count
        
        return finalCount