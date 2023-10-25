class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        arr=[]
        for i in nums:
            if not nums.count(i)>1:
                arr.append(i)
        def sum(x,y):
            return x+y
        if not len(arr)>0:
            return 0
        sum = reduce(sum , arr)
        return sum