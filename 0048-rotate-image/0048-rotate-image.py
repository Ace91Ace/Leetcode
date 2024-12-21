class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        def transpose(mat):
            for i in range(n):
                for j in range(i+1, n):
                    mat[i][j], mat[j][i] = mat[j][i],mat[i][j]


        transpose(matrix)
        for i in range(n):
            matrix[i] = matrix[i][::-1]
            
            
            
            

        