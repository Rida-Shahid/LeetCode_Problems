class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0


        for row in grid:
            temp=len(row)
            for i in range(0,temp):
                if row[i] < 0:
                    count += temp-i
                    break
        return count





        