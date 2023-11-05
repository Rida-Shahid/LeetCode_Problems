class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total_sum=0
        size=len(nums)  
        num=0
        for i in range(0,size):
            sub_arr=set()
            for j in range(i,size):
                sub_arr.add(nums[j])
                num= len(sub_arr)
                total_sum += num*num
        return total_sum
                

            


        