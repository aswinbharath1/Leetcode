class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mapping = { piece[0] : piece for piece in pieces }
        res=[]
        for i in arr:
            res += mapping.get(i, [])
        return arr == res