class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum=0
        digit_sum=0
        remainder=0
        quo=0
        diff=0
        val=0
        for i in nums:
            element_sum = element_sum + i
            while i > 0:
                remainder = i % 10
                digit_sum += remainder
                i //= 10 
        diff= abs(element_sum-digit_sum)
        return diff

        



        