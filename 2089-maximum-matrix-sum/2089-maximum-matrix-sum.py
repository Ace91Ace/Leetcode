class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ts = 0
        minv = float('inf')
        n = 0

        for i in matrix:
            for j in i:
                ts += abs(j)

                if j < 0:
                    n += 1
                minv = min(minv,abs(j))

        return ts - 2*minv if n%2 != 0 else ts