class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        maxi_value=0
        nums.sort(reverse=True)
        maxi_value=(nums[0]-1)*(nums[1]-1)
        return maxi_value
        