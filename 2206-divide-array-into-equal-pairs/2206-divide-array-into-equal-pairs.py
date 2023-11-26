class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        new_dict ={}
        total=0
        for element in nums:
            if element not in new_dict:
               new_dict[element] = 1
            else:
                new_dict[element] += 1
        for value in new_dict.values():
            if value%2==0:
                total += value             
        if total == len(nums):
            return True
        else:
            return False


        