class Solution:
    def isGood(self, nums: List[int]) -> bool:
        base= [i for i in range(1, len(nums))]
        base.append(len(nums)-1)
        nums.sort()
        return nums == base
