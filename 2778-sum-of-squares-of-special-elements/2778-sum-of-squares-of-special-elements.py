class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        total_sum=0
        total=0
        n=len(nums)

        for i in range(1,n+1):
            if (n % i == 0):
                total = nums[i-1] * nums[i-1]
                total_sum += total
            
        return total_sum
        