class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total_sum=0
        size=len(arr)
        for i in range(0,size):
            for j in range(i,size,2):
                total_sum += sum(arr[i:j+1])
        return total_sum
            

