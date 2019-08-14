class Solution:
    def isValid(self, s: str) -> bool:
        lefts = ['(', '{', '[']
        rights = [')', '}', ']']
        mapping = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        # print(mapping['('])
        
        stack = []
        i = 0
        
        if len(s) == 1:
            return False
        while i < len(s):
            # Base case
            if len(stack) == 0:
                if s[i] in rights:
                    return False
                stack.append(s[i])
            # General case
            elif mapping[stack[-1]] == s[i]:
                stack.pop()
            elif s[i] in lefts:
                stack.append(s[i])
            else:
                return False
            i += 1

        if len(stack) == 0:
            return True