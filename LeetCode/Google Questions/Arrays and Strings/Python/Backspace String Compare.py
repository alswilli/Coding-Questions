class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def transform(string):
            i = 0
            while i < len(string):
                print(i)
                if string[i] == "#":
                    # Delete curr and prev if prev index is > -1 and i+1 < len(string)
                    if i > 0 and i+1 < len(string):
                        string = string[:i-1] + string[i+1:]
                        i -= 1
                    elif i+1 < len(string): # if its only #
                        string = string[i+1:]
                    elif i > 0: # if there are still more chars
                        string = string[:i-1]
                        i -= 1
                    else:
                        string = ""
                else:
                    i += 1
            return string
                
                        
        
        newS = transform(S)
        newT = transform(T)
        print("New S:" + newS)
        print("New T:" + newT)
        if newS == newT:
            return True
        return False

#         def transform(string):
#             newS = ""
#             for char in string:
#                 if char == "#":
#                     if len(newS) != "":
#                         newS = newS[:-1]
#                 else:
#                     newS = newS + char
#             return newS
        
#         newS = transform(S)
#         newT = transform(T)
#         if newS == newT:
#             return True
#         return False
        