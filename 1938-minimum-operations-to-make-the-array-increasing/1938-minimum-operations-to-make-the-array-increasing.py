class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        count = current = 0
        for i in nums:
            if i <= current :
                current += 1
                count += current-i
            else:
                current = i
        return count