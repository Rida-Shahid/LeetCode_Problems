class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        res=[0] * len(nums)
        even_index=[]
        odd_index=[]
        for i in range(0,len(nums)):
            if i%2==0:
                even.append(nums[i])
                even_index.append(i)
            else:
                odd.append(nums[i])
                odd_index.append(i)
        odd.sort(reverse = True)
        even.sort()
        for i in range(len(even)):
            res[even_index[i]]=even[i]
        for j in range(len(odd)):
            res[odd_index[j]]=odd[j]
        
        
        return res
        
        