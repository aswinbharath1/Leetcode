class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s , e = -1 , -1
        for i in range(len(nums)):
            if nums[i]==target:
                s=i
                break
        if s==-1:
            return [-1,-1]
        
        for i in range (len(nums) -1,-1,-1):
            if nums[i]==target:
                e = i
                break

        return [s,e]