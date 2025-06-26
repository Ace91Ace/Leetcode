class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        prevs = self.generate(numRows-1)
        prev = [0]+prevs[-1]+[0]
        res = [prev[i]+prev[i+1] for i in range(len(prev)-1)]
        prevs.append(res)
        return prevs
