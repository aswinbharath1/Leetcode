class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        c=0
        for i in range(0,len(startTime)):
            if(queryTime in range(startTime[i],endTime[i]+1)):
                c+=1
        return c