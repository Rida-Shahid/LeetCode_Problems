class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        size= len(nums)
        answer=[]
        leftsum=[0] * size
        
        rightsum=[0] * size
        
        for i in range(1,size):
            leftsum[i]= leftsum[i-1]+ nums[i-1] 
        for i in range(size-2,-1,-1):
            rightsum[i]= rightsum[i+1] + nums[i+1]
        for i in range(size):
            answer.append(abs(leftsum[i] - rightsum[i]))
        return answer


        