class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(s):
            return s == s[::-1]
        p=[]
        for i in range ( len(s)):
            for j in range (i, len(s)):
                sub = s[i:j+1]
                if is_palindrome(sub):
                    if len(p)>len(sub):
                        continue
                    else:
                        p = sub
        return p