class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        new_list=[]
        for i in nums:
            for j in str(i):
                new_list.append(int(j))
        return new_list