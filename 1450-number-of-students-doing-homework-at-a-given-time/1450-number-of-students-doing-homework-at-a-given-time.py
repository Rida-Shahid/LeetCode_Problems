class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count=0
        start=0
        end=0
        for i in range(0,len(startTime)):
            start= startTime[i]
            end = endTime[i]
            if start <= queryTime and end >= queryTime:
                count +=1
        return count
        