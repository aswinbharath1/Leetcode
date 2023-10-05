class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        x=[i for i in set(nums) if nums.count(i)> (len(nums)//3) ]
        return x