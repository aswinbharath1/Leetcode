class Solution:
    def findLucky(self, arr: List[int]) -> int:
        x=0
        f=[]
        for i in range(len(arr)):
            if arr.count(arr[i])==arr[i]:
                x+=1
                f.append(arr[i])
        if x==0:
            return -1
        else:
            f=sorted(f)
            return f[-1]