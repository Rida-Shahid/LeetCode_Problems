class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        size= len(nums)
        sum1=0
        sum2=0
        count=0


        for i in range(0,size):
            for j in range(1,size):
                sum1=nums[j]-nums[i]
                for k in range(2,size):
                    sum2= nums[k] - nums[j]
                    if(sum1==sum2 and sum1==diff):
                        count = count+1
        return count



        