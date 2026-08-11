class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        cols=len(matrix[0])
        row_z=[False]*row
        col_z=[False]*cols
        for i in range(row):
            for j in range(cols):
                if matrix[i][j]==0:
                    row_z[i]=True
                    col_z[j]=True
        for i in range(row):
            for j in range(cols):
                if row_z[i] or col_z[j]:
                    matrix[i][j]=0
        return matrix