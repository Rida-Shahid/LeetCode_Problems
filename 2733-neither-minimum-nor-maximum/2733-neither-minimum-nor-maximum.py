class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        if n > 2:
            return nums[1]
        else:
            return -1

       
        