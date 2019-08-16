class Solution:
	# Time Olen(s) + len(t)
	# Space Olen(s) + len(t)
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        countT = collections.Counter(t)
        fillter = []
        for i,char in enumerate(s):
            if char in countT:
                fillter.append((i,char))
        #print(fillter)
        required = len(countT)
        done = 0
        l = r = 0
        res = ""
        window = collections.Counter()
        rMove = True
        while r < len(fillter):
            char = fillter[r][1]
            window[char] += 1
            #print(fillter[l],fillter[r],window,rMove)

            if window[char] == countT[char]:
                done += 1
            #print(done)
            while l <= r and done == required:
                if (res == "" or len(res) > fillter[r][0] - fillter[l][0] + 1):
                    res = s[fillter[l][0]:fillter[r][0]+1]
                left = fillter[l][1]
                window[left] -= 1
                if window[left] < countT[left]:
                    done -= 1
                l += 1
                
            
            r += 1
        return res