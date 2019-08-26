class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        def recurseNums(output, digits, currStr):
            if len(digits) == 1:
                for letter in LtoA[digits[0]]:
                    nextStr = currStr + letter
                    output.append(nextStr)
                return output

            for letter in LtoA[digits[0]]:
                nextStr = currStr + letter
                output = recurseNums(output, digits[1:], nextStr)
                
            return output
        
        LtoA = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"],
        }
        if len(digits) == 0:
            return []
        
        if len(digits) == 1:
            return LtoA[digits[0]]
        
        output = []
        currStr = ""
        for letter in LtoA[digits[0]]:
            nextStr = currStr + letter
            output = recurseNums(output, digits[1:], nextStr)
            
        return output