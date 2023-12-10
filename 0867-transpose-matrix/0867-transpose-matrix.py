class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows= len(matrix)
        cols= len(matrix[0])
        res_mat = [[0] * rows for _ in range(cols)]
        for i in range(0,rows):
            for j in range(0,cols):
                res_mat[j][i] = matrix[i][j]
        return res_mat


        