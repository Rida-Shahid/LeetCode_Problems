class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        total_sum=0
        moves=0
        nums.sort(reverse=True)
        while k > 0  :
            total_sum += nums[0]
            nums[0]= nums[0] + 1
            k = k-1
        return total_sum

        