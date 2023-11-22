class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp_list= list(heights)
        exp_list.sort()
        count=0

        for i in range(0,len(heights)):
            if exp_list[i] != heights[i]:
                count +=1
        return count
        