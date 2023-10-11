class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
		
        answer = float("+inf")
        for i, start in enumerate(nums):
            
            search = start + n - 1  # number to search
            start, end = 0, len(nums)-1
            
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] <= search:
                    idx = mid
                    start = mid + 1
                else:
                    end = mid - 1
            
            changes = idx - i + 1
            answer = min(answer, n - changes)
        return answer
                