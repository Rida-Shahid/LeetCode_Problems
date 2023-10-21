class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        length= len(hours)
        hours.sort()
        print(hours)
        for index , i in enumerate(hours):
            if(i >= target):
                return (length-index)
            else:
                continue
        return 0
        

        