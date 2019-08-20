# class Solution:
#     def decodeString(self, s: str) -> str:
#         # Find the number
#         # While brackets are open, gather the contents
#         # If you find another number, call recursively
#         # Return when closing bracket reached
#         # Continue searching for number (if on outside of loop) or collecting till end of string and/or inner closing bracket 
        
#         def numRecurse(i, letters, numbers):
#             # global i
#             print("NUMBERS: " + str(numbers))
#             total = ""
#             # print(numbers)
#             # print(i)
#             total = total + s[i]
#             j = i + 1
#             while s[j].isdigit():
#                 total = total + s[j]
#                 j += 1
#             numbers.append(int(total))
#             print(numbers)
#             i = j+1  # bypass open brace
#             # letters = ""
#             while s[i] != "]":
#                 if s[i].isdigit():
#                     letters, numbers = numRecurse(i, letters, numbers)
#                 else:
#                     letters = letters + s[i]
#                     print(letters)
#                 i += 1
#             num = numbers[-1]
#             letters = 3 * letters
#             numbers.pop(-1)
#             i += 1
#             return letters, numbers
#         # global i 
#         i = 0
#         numbers = []
#         letters = ""
#         while i < len(s):
#             letters, numbers = numRecurse(i, letters, numbers)
#         print(letters)
#         return letters

class Solution:
    def decodeString(self, s: str) -> str:
        if not s: return ''
        k = ''
        stack = []
        res = ''
        for i in range(len(s)):
            if s[i] == '[':
                stack.append(i)
                print(stack)
            elif s[i] == ']':
                index = stack.pop()
                if not stack:
                    return res + (int(k) * self.decodeString(s[index+1:i])) + self.decodeString(s[i+1:])
            print("out")
            if not stack:
                print("in")
                print(stack)
                if '0' <= s[i] <= '9':
                    k += s[i]
                    print(k)
                else:
                    res += s[i]
                    print(res)
        return res