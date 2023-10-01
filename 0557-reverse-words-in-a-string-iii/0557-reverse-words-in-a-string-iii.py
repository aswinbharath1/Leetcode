class Solution:
    def reverseWords(self, s: str) -> str:
        splits=s.split()
        res=[]
        for i in splits:
            res.append(''.join(reversed(list(i))))
        result=' '.join(res)
        return result
