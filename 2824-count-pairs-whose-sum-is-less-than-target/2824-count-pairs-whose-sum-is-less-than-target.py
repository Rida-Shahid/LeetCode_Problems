class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        length = len(nums)
        count=0
        for i in range(length):
            for j in range(i+1,length):
                if(nums[i] + nums[j] < target):
                    count=count+1                  
            else:
                continue     
        return count

        