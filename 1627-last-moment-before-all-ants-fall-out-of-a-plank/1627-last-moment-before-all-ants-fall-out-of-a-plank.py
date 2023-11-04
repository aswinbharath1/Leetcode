class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        res = 0 
        for i in left:
            res = max(res , abs(0 - i))
        for i in right:
            res = max(res , abs(n - i))
        return res