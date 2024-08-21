class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        A = matrix
        x = len(A)
        y = len(A[0])

        lis = []

        cx = math.ceil(x / 2)
        cy = math.ceil(y / 2)

        for t in range(min(cx, cy)):
            for i in range(t, y - t):
                lis.append(A[t][i])

            for i in range(t + 1, x - t):
                lis.append(A[i][y - t - 1])

            if x - t - 1 > t:
                for i in range(y - t - 2, t - 1, -1):
                    lis.append(A[x - t - 1][i])

            if y - t - 1 > t:
                for i in range(x - t - 2, t, -1):
                    lis.append(A[i][t])

        return lis
