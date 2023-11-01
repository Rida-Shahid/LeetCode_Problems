class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        res=0
        n=len(nums) 
        for i in range(0,n):
            for j in range(i+1,n):
                res= abs(nums[i]-nums[j])
                if(res==k):
                    count=count+1
                else:
                    continue
        return count

            
        