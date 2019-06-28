class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        count = 0
        
        for o, num in enumerate(A):
            # i = A.index(num)
            i = o
            print(i)
            jump = "odd"
            valid = True
            while i < len(A) - 1:
                if jump == "odd":
                    # minV = min(A[i+1:])
                    check = A[i+1:]
                    print(check)
                    minV = (0, 10000)
                    for w, val in enumerate(check):
                        if val >= A[i] and val < minV[1]:
                            minV = (w+i+1, val)
                    print("minV: " + str(minV[1]))
                    if minV[1] >= A[i] and minV[1] != 10000:
                        # i = A.index(minV)
                        i = minV[0]
                        print("odd: " + str(i))
                        jump = "even"
                    else:
                        valid = False
                else: #jump == "even":
                    # maxV = max(A[i+1:])
                    maxV = (0, -1)
                    check = A[i+1:]
                    print(check)
                    for w, val in enumerate(check):
                        if val <= A[i] and val > maxV[1]:
                            maxV = (w+i+1, val)
                    print("maxV: " + str(maxV[1]))
                    if maxV[1] <= A[i] and maxV[1] != -1:
                        # i = A.index(maxV)
                        i = maxV[0]
                        print("even: " + str(i))
                        jump = "odd"
                    else:
                        valid = False
                if valid == False:
                    break
            if valid == True:
                print("good: " + str(i))
                count += 1
            print("next")
            print()
        
        return count