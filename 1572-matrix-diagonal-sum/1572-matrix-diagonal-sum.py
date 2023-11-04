class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total_sum=0
        size= len(mat)
        for i in range(0,size):
            total_sum += mat[i][i]
            if (i != size-1-i):
                total_sum += mat[i][size-1-i]
        return total_sum

        