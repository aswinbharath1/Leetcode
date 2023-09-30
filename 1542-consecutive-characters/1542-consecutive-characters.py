class Solution:
    def maxPower(self, s: str) -> int:
        curr = 1 
        maxp = 1  
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                curr = 1
            maxp = max(maxp, curr)

        return maxp