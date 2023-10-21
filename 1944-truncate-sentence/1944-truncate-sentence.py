class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split(' ')
        arr = ' '.join( s[:k]) 
        return arr