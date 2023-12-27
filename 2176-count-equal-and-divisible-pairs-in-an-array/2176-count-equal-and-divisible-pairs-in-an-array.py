class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count=0
        mul=0

        for i in range(0,len(nums)-1):
            for j in range(1,len(nums)):
                if i<j:
                    mul = i*j
                    if nums[i] == nums[j] and mul % k == 0:
                        count += 1
            
                    
        return count

        