class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        total_sum=0
        new_dict={}

        for element in nums:
            if element not in new_dict:
                new_dict[element] = 1
            else:
                new_dict[element] += 1
        for element in new_dict:
            if new_dict[element] == 1:
                total_sum += element
            else:
                continue
        return total_sum

        