class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key = lambda x: x[1])
        items = items[::-1]
        res = []

        for i in queries:
            flag = 0
            for j in items:
                if j[0] <= i:
                    res.append(j[1])
                    flag = 1
                    break
            if not flag :
                res.append(0)

        return res

    

        