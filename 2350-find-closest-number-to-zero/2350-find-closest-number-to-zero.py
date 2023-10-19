class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        c= 1000000
        for i in nums :
            if abs(c) >=  abs (i) :
                if abs(c) == abs(i):
                    if i>c:
                        c=i
                else:
                    c=i
        return c


        
