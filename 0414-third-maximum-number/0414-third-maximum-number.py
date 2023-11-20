class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        new_set = set(nums)
        new_list= list(new_set)
        new_list.sort(reverse=True)
        if len(new_list) < 3:
            return new_list[0]
        else:
            return new_list[2]
        