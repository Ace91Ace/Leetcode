class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def help(i):
            if i == 0:
                return []
            if i == 1:
                return [[1]]
            prev = help(i-1)
            p = [0]+prev[-1]+[0]
            res = [p[i]+p[i+1] for i in range(len(p)-1)]
            prev.append(res)
            return prev
        return help(rowIndex+1)[-1]