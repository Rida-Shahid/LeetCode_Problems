class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        

        for i in nums:
            digit_count=0
            while i > 0:
                remainder = i % 10
                digit_count += 1
                i //= 10 
            if digit_count % 2 == 0:
                count +=1
            else:
                continue
        return count
        
        