class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        cd=arr[1]-arr[0]
        for i in range(1,len(arr)):
            if (arr[i]-arr[i-1])!=cd:
                return False
        return True