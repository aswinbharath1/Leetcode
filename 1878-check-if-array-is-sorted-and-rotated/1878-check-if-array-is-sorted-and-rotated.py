class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        left, right = 0, n - 1
        while left < right and nums[left] == nums[right]:
            left += 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left
        return nums == sorted(nums) or nums[pivot:] + nums[:pivot] == sorted(nums)
