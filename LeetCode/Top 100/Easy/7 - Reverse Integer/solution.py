class Solution:
    def reverse(self, x: int) -> int:
        numbers = []
        
        orig = x
        if orig < 0:
            x = x * -1
        
        while x != 0:
            currNum = x % 10
            numbers.append(int(currNum))
            x = (x - currNum) / 10
        
        print(numbers)
        
        i = len(numbers)-1
        finalNum = 0
        tens = 1
        while i > -1:
            finalNum += numbers[i] * tens
            tens = tens * 10
            i -= 1
        if orig < 0:
            finalNum = finalNum * -1
        if finalNum > (pow(2, 31) - 1) or finalNum < (pow(2, 31) * -1):
            return 0
        return finalNum